# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавить в нее систему логирования из лекции(в отдельный файл записывается, кто, во сколько и какое сообщение отправил)
# Для действительных (+, -, /, %, // , "умножить") Для рациональных (+, -, /, "умножить)

import telebot
from telebot import types
import datetime as dt


name_file = 'calculator_bot/log_file.csv'
bot = telebot.TeleBot("5906527884:AAEDLxC4R_VycmB6gabilLQl4mSAbdw405Q")
num1 = 0
num2 = 0
type_num = ''


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет. Калькулятор включен!")
    button(message)


@bot.message_handler(commands=["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Целые числа")
    but2 = types.KeyboardButton("Комплексные числа")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(
        message.chat.id, "Выберите с какими числами будете работать", reply_markup=markup)
    bot.register_next_step_handler(message, init_type_num)



def init_type_num(message):
    global type_num
    type_num = str(message.text)
    if (type_num == "Целые числа"):
        bot.send_message(message.chat.id, "Введите целое число")
        bot.register_next_step_handler(message, init_num1)
    else:
        bot.send_message(
            message.chat.id, "Введите комплексное число, пример: 3j, 5-3j")
        bot.register_next_step_handler(message, init_num1)


def init_num1(message):
    global num1, type_num
    log_actions(message)
    if (type_num == "Целые числа"):
        num1 = int(message.text)
        bot.send_message(message.chat.id, "Введите второе целое число")
        bot.register_next_step_handler(message, button_init)
    else:
        num1 = complex(message.text)
        bot.send_message(message.chat.id, "Введите второе комплексное число")
        bot.register_next_step_handler(message, button_init)

def button_init(message):
    global num2, type_num
    log_actions(message)

    if (type_num == "Целые числа"):
        num2 = int(message.text)
    else:
        num2 = complex(message.text)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("+")
    but2 = types.KeyboardButton("-")
    but3 = types.KeyboardButton("*")
    but4 = types.KeyboardButton("/")
    if (type_num == "Целые числа"):
        but5 = types.KeyboardButton("%")
        but6 = types.KeyboardButton("//")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    if (type_num == "Целые числа"):
        markup.add(but5)
        markup.add(but6)
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)
    bot.register_next_step_handler(message, operators)


@bot.message_handler(content_types="text")
def operators(message):
    global num1, num2
    log_actions(message)
    result = 0
    if message.text == "+":
        result = num1 + num2
        bot.send_message(message.chat.id, f'{num1} + {num2} = {result}')
    elif message.text == "-":
        result = num1 - num2
        bot.send_message(message.chat.id, f'{num1} - {num2} = {result}')
    elif message.text == "*":
        result = num1 * num2
        bot.send_message(message.chat.id, f'{num1} * {num2} = {result}')
    elif message.text == "/":
        result = num1 / num2
        bot.send_message(message.chat.id, f'{num1} / {num2} = {result}')
    elif message.text == "%":
        result = num1 % num2
        bot.send_message(message.chat.id, f'{num1} % {num2} = {result}')
    elif message.text == "//":
        result = num1 // num2
        bot.send_message(message.chat.id, f'{num1} // {num2} = {result}')


def log_actions(message):
    time_sign = dt.datetime.now().strftime('%D %H:%M')
    file = open(name_file, 'a')
    file.write(
        f'{time_sign},{message.chat.username},{message.chat.id},{message.text}\n')
    file.close()


bot.infinity_polling()
