import telebot
from telebot import types
import requests
import json

import admins

baseURL = "https://fakestoreapi.com"
if __name__ == "__main__":
    bot = telebot.TeleBot("6342244998:AAEfTjyeKwBQtadMfGfDYchZxSESt0Vs-tI")
    users = {}


    def main_reply_menu():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(types.KeyboardButton("Показати продукти"))

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

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(msg):
        # bot.reply_to(message, "Howdy, how are you doing?")
        cid = msg.chat.id
        bot.send_message(cid, "Hello !", reply_markup=main_reply_menu())


    @bot.message_handler(commands=['admin'])
    def admin_commands(msg):
        admin = admins.ADMINS
        cid = msg.chat.id
        if cid in admin:
            bot.reply_to(msg, "Admin activated", reply_markup=admin_reply_menu())

    @bot.message_handler(func=lambda message: True)
    def echo_all(msg):
        encounter = 1
        admin = admins.ADMINS
        cid = msg.chat.id
        if msg.text == "Показати продукти":
            text = get_product()
            bot.send_message(cid, text)
        if msg.text == "Показати 1 продукт" and cid in admin:
            question = bot.send_message(cid, "Введіть ID продукта: ")
            bot.register_next_step_handler(question, show_one_product)


    bot.infinity_polling()

    response = requests.get(f"{baseURL}/products")

    data = response.json()

    print(data)
    # for i in data:
    #     price = i['price']
    #     title = i['title']
    #     id = i['id']
    #     print(f"{id}. {title} -- {price}\n")

    new_product = {
        'title': 'test product',
        "price": 13.5,
        "description": 'lorem ipsum set',
        'image': 'https://i.pravatar.cc',
        'category': 'electronic'
    }

    resp = requests.post(f"{baseURL}/products", data=new_product)

    id = 5
    resp = requests.delete(f"{baseURL}/products/{id}")

    print(resp.text)
