# Основное - сделать бота для игры с конфетами между человеком и телеграмм ботом

import telebot
from telebot import types
import datetime
import random

bot = telebot.TeleBot("5906527884:AAEDLxC4R_VycmB6gabilLQl4mSAbdw405Q")
sweets = 221
max_sweet = 28
user_turn = 0
bot_turn = 0
flag = ''
lvl_bot = ''


@bot.message_handler(commands=["start"])
def start(message):
    global flag, sweets
    bot.send_message(message.chat.id, "Игра в конфеты.")

    bot.send_message(message.chat.id, f"Введите общее количество конфет")
    bot.register_next_step_handler(message, init_var_sweets)


def init_var_sweets(message):
    global sweets
    sweets = int(message.text)
    bot.send_message(
        message.chat.id, f"Введите максимальное количество конфет за ход")
    bot.register_next_step_handler(message, init_var_max_sweets)


def init_var_max_sweets(message):
    global max_sweet
    max_sweet = int(message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("bot stupid")
    but2 = types.KeyboardButton("bot smart")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(
        message.chat.id, "Выбери уровень бота ниже", reply_markup=markup)
    bot.register_next_step_handler(message, choosing_move)


def choosing_move(message):
    global flag, lvl_bot
    lvl_bot = str(message.text)

    flag = random.choice(['user', 'bot'])
    if flag == 'user':
        bot.send_message(message.chat.id, "Ходит пользователь")
        controller(message)

    else:
        bot.send_message(message.chat.id, "Ходит бот")
        controller(message)


def controller(message):
    global flag, lvl_bot
    if sweets > 0:
        if flag == 'user':
            bot.send_message(
                message.chat.id, f"Ваш ход введите количество конфет от 0 до - {max_sweet}")
            bot.register_next_step_handler(message, user_import)
        elif flag == 'bot' and lvl_bot == "bot smart":
            bot_imput(message)
        else:
            bot_imput_stupid(message)
    else:
        flag = 'user' if flag == 'bot' else 'bot'
        bot.send_message(message.chat.id, f"Победил - {flag}")


def user_import(message):
    global flag, user_turn, sweets
    user_turn = int(message.text)
    sweets -= user_turn
    bot.send_message(message.chat.id, f"осталось {sweets}")
    flag = 'user' if flag == 'bot' else 'bot'
    controller(message)


def bot_imput(message):
    global sweets, bot_turn, flag
    if sweets <= max_sweet:
        bot_turn = sweets
    elif sweets % max_sweet == 0:
        bot_turn = max_sweet-1
    else:
        bot_turn = sweets % max_sweet-1
        if bot_turn == 0:
            bot_turn = 1
    sweets -= bot_turn
    bot.send_message(message.chat.id, f"Бот взял - {bot_turn}")
    bot.send_message(message.chat.id, f"Осталось - {sweets}")
    flag = 'user' if flag == 'bot' else 'bot'
    controller(message)


def bot_imput_stupid(message):
    global sweets, bot_turn, flag
    bot_turn = random.randint(1, max_sweet)
    sweets -= bot_turn
    bot.send_message(message.chat.id, f"Бот взял - {bot_turn}")
    bot.send_message(message.chat.id, f"Осталось - {sweets}")
    flag = 'user' if flag == 'bot' else 'bot'
    controller(message)


bot.infinity_polling()
