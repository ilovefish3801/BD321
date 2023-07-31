import telebot
from telebot import types

if __name__ == "__main__":

    bot = telebot.TeleBot("6342244998:AAEfTjyeKwBQtadMfGfDYchZxSESt0Vs-tI")


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


    def main_reply_menu():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # itembtn1 = types.KeyboardButton('a')
        # itembtn2 = types.KeyboardButton('v')
        # itembtn3 = types.KeyboardButton('d')
        # markup.add(itembtn1, itembtn2, itembtn3)
        markup.row(types.KeyboardButton("BTN 1"), types.KeyboardButton("BTN 2"), types.KeyboardButton("BTN 3"))
        markup.row(types.KeyboardButton("Прості числа"))
        return markup


    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(msg):
        # bot.reply_to(message, "Howdy, how are you doing?")
        cid = msg.chat.id
        bot.send_message(cid, "Hello !", reply_markup=main_reply_menu())


    @bot.message_handler(func=lambda message: True)
    def echo_all(msg):
        cid = msg.chat.id
        # bot.reply_to(message, message.text)
        if msg.text == "Прості числа":
            numbers = primeNumbers(1, 100)
            temp_text = "Список простих чисел: \n\n"
            for num in numbers:
                temp_text += f"{num} "

            bot.send_message(cid, temp_text)


    bot.infinity_polling()
