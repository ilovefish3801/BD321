import telebot
from telebot import types

if __name__ == "__main__":
    if __name__ == "__main__":

        bot = telebot.TeleBot("6342244998:AAEfTjyeKwBQtadMfGfDYchZxSESt0Vs-tI")
        users = {}

        def getName(msg):
            cid = msg.chat.id
            txt = msg.text
            users[f"{cid}"] = {}
            users[f"{cid}"]["name"] = txt
            mess = bot.send_message(cid, "Enter your age: ")
            bot.register_next_step_handler(mess, getAge)

        def getAge(msg):
            cid = msg.chat.id
            age = msg.text
            users[f"{cid}"]["age"] = age
            bot.send_message(cid, "Thanks for answering this survey", reply_markup=main_reply_menu())
            print(users)

        def primeNumbers(star_value, end_value):
            simpleNum = []
            for i in range(star_value, end_value):
                flag = True
                for j in range(star_value, end_value):
                    if j != 1 and i != j and j <= i:
                        result = i % j
                        if result == 0:
                            flag = False
                            break
                if flag:
                    simpleNum.append(i)
            return simpleNum


        def subMenu():
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row(types.KeyboardButton("BTN 1"), types.KeyboardButton("BTN 2"), types.KeyboardButton("Підменю 2"))
            markup.row(types.KeyboardButton("BTN 4"), types.KeyboardButton("BTN 5"))
            markup.row(types.KeyboardButton("Назад"))
            return markup


        def subMenuTwo():
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row(types.KeyboardButton("BTN 1"), types.KeyboardButton("BTN 2"), types.KeyboardButton("Підменю2"))
            markup.row(types.KeyboardButton("BTN 4"), types.KeyboardButton("BTN 5"))
            markup.row(types.KeyboardButton("Назад"), types.KeyboardButton("Назад до головного меню"))
            return markup


        def main_reply_menu():
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row(types.KeyboardButton("Inline Menu"), types.KeyboardButton("Підменю"),
                       types.KeyboardButton("Ask me"))
            markup.row(types.KeyboardButton("Прості числа"))
            return markup


        def inline_keyboard():
            inline = types.InlineKeyboardMarkup()
            btnOne = types.InlineKeyboardButton("BTN ONE", callback_data="btnOne")
            btnTwo = types.InlineKeyboardButton("BTN TWO", callback_data="btnTwo")
            inline.row(btnOne, btnOne)
            inline.row(btnTwo)
            return inline


        @bot.callback_query_handler(func=lambda call: True)
        def inline_menu(call):
            cid = call.message.chat.id
            data = call.data
            if data == "btnOne":
                bot.send_message(cid, "<u>Succesfully pressed button number one</u>", parse_mode="HTML")
            elif data == "btnTwo":
                bot.send_photo(cid, open("RyanGosling.jpg", "rb"), caption="test")

            print(cid, data)


        @bot.message_handler(commands=['start', 'help'])
        def send_welcome(msg):
            # bot.reply_to(message, "Howdy, how are you doing?")
            cid = msg.chat.id
            bot.send_message(cid, "Hello !", reply_markup=main_reply_menu())


        @bot.message_handler(func=lambda message: True)
        def echo_all(msg):
            encounter = 1

            cid = msg.chat.id
            # bot.reply_to(message, message.text)
            if msg.text == "Прості числа":
                numbers = primeNumbers(1, 100)
                temp_text = "Список простих чисел: \n\n"
                for num in numbers:
                    temp_text += f"{num} "
            if msg.text == "Підменю":
                menu = "subMenu"
                bot.reply_to(msg, "Підменю відкрито", reply_markup=subMenu())
            elif msg.text == "Назад":
                bot.reply_to(msg, "Повертаю назад", reply_markup=main_reply_menu())

            elif msg.text == "Inline Menu":
                bot.send_message(cid, "Inline Menu Test", reply_markup=inline_keyboard())
            elif msg.text == "Ask me":
                mess = bot.send_message(cid, "Tell me your name: ")
                bot.register_next_step_handler(mess, getName)

        bot.infinity_polling()
