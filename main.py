import telebot
from telebot import types

import requests

import admins

import json

baseURL = "https://fakestoreapi.com"
exchangeURL = "https://bank.gov.ua/NBUStatService/v1"

converter_data = {}
currency_data = []
if __name__ == "__main__":
    bot = telebot.TeleBot("6342244998:AAEfTjyeKwBQtadMfGfDYchZxSESt0Vs-tI")


    def main_reply_menu():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(types.KeyboardButton("Показати продукти"), types.KeyboardButton("Конвертер валют"))

        return markup


    def admin_reply_menu():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(types.KeyboardButton("Показати 1 продукт"))

        return markup


    def get_product():
        response = requests.get(f"{baseURL}/products")

        data = response.json()

        wholePrice = 0
        text = ''
        for i in data:
            price = i['price']
            title = i['title']
            id = i['id']
            text += f"{id}. {title} -- {price}\n"
        return text


    def show_one_product(msg):
        id = msg.text
        resp = requests.get(f"{baseURL}/products/{int(id)}")
        bot_resp = resp.text

        return bot.reply_to(msg, bot_resp)


    def get_data_currency():
        LINK = f"{exchangeURL}/statdirectory/exchange?json"
        responce = requests.get(LINK)

        exchangeData = responce.json()

        # 978 - EUR
        # 840 - USD
        for i in exchangeData:
            currency_data.append(i)
        print(currency_data)


    def r_converter():
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        counter = 0
        buttons = []
        for curr in currency_data:
            counter += 1
            btn = types.KeyboardButton(f"{curr['txt']}")
            buttons.append(btn)
            if counter == 3:
                kb.row(buttons[0], buttons[1])
                counter = 0
                buttons = []
        return kb


    def set_choice_curr(msg):
        converter_data["currency"] = msg.text
        cid = msg.chat.id
        mess = bot.send_message(cid, "Введіть суму для обміну: ", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(mess, set_amount_curr)


    def set_amount_curr(msg):
        cid = msg.chat.id

        converter_data["amount"] = msg.text
        currency_object = None
        for item in currency_data:
            if item['txt'] == converter_data['currency']:
                currency_object = item.copy()
                break

        result = float(converter_data['amount']) / float(currency_object['rate'])
        result = round(result, 2)
        bot.send_message(cid, f"{currency_object['cc']} : {result}", reply_markup=main_reply_menu())


    def save_user(cid):
        with open("users.json", 'r') as f:
            users = json.load(f)

        if cid not in users:
            users.append(cid)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    @bot.message_handler(commands=['spam'])
    def send_spam(msg):
        with open('users.json', 'r') as f:
            users = json.load(f)
        for id in users:
            try:
                bot.send_message(id, "spam")
            except Exception as err:
                print(err)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(msg):
        cid = msg.chat.id
        save_user(cid)
        bot.send_message(cid, "Hello !", reply_markup=main_reply_menu())


    @bot.message_handler(commands=['admin'])
    def admin_commands(msg):
        admin = admins.ADMINS
        cid = msg.chat.id
        if cid in admin:
            bot.reply_to(msg, "Admin activated", reply_markup=admin_reply_menu())


    @bot.message_handler(func=lambda message: True)
    def echo_all(msg):
        admin = admins.ADMINS
        cid = msg.chat.id
        if msg.text == "Показати продукти":
            text = get_product()
            bot.send_message(cid, text)
        elif msg.text == "Показати 1 продукт" and cid in admin:
            question = bot.send_message(cid, "Введіть ID продукта: ")
            bot.register_next_step_handler(question, show_one_product)
        elif msg.text == "Конвертер валют":
            get_data_currency()
            mess = bot.send_message(cid, "Оберіть валюту, яку бажаєте обміняти", reply_markup=r_converter())
            bot.register_next_step_handler(mess, set_choice_curr)


    bot.infinity_polling()
