import telebot
from telebot import types
import requests
import json
import pandas as pd
from pandas import DataFrame
import openpyxl
import admins
import time
import datetime

baseURL = "https://fakestoreapi.com"
if __name__ == "__main__":
    bot = telebot.TeleBot("")
    users = {}



    def main_reply_menu():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(types.KeyboardButton("Показати продукти"), types.KeyboardButton("Надіслати файл"))

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
        elif msg.text == "Надіслати файл":
            file = open("data.xlsx", "rb")
            bot.send_document(cid, file)

    # bot.infinity_polling()
# Pandas
data = {
    'Name': ["John", "Jane", "Jack"],
    'Age': [25, 26, 11],
    'City': ["New York", "LA", "New York"]
}

df = pd.DataFrame(data)

exel_file_path = f"data{datetime.datetime.now().date()}.xlsx"

df.to_excel(exel_file_path, index=False)

# df = pd.read_excel(exel_file_path)

# Reading excel file (turning it back to dictionary)
# for _, row in df.iterrows():
#     print(row['Name'], row['Age'], row['City'])
