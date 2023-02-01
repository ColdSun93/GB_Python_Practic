# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавить в нее систему логирования из лекции(в отдельный файл записывается, кто, во сколько и какое сообщение отправил) 
# Для действительных (+, -, /, %, // , "умножить") Для рациональных (+, -, /, "умножить)

import telebot
from telebot import types
import datetime
import random

bot = telebot.TeleBot("5906527884:AAEDLxC4R_VycmB6gabilLQl4mSAbdw405Q")


@bot.message_handler(commands=["start"])
def start(message):
    global flag, sweets
    bot.send_message(message.chat.id, "Калькулятор.")
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # but1 = types.KeyboardButton("bot stupid")
    # but2 = types.KeyboardButton("bot smart")
    # markup.add(but1)
    # markup.add(but2)
    # bot.send_message(
    #     message.chat.id, "Выбери уровень бота ниже", reply_markup=markup)
    # bot.register_next_step_handler(message, choosing_move)



# def button_click():
#     type = view.get_module()
#     value_a = view.get_value(type)
#     value_b = view.get_value(type)
#     operator = view.get_operation(type)
#     model.init(value_a, value_b)
#     if operator=='+':
#         result = model.do_it_sum()
#     elif operator=='-':
#         result = model.do_it_sub()
#     elif operator=='*':
#         result = model.do_it_multi()
#     elif operator=='/':
#         result = model.do_it_div()
#     elif operator=='//':
#         result = model.do_it_div_rem()
#     elif operator=='%':
#         result = model.do_it_div_mod()
#     view.view_data(result, "resul")
    