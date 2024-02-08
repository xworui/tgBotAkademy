from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton('Задать доп вопрос'),
        KeyboardButton('3Ds max')
    )
    return keyboard

def get_main_3dmax_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    keyboard.add(
        KeyboardButton('Часто задаваемые вопросы'),
        KeyboardButton('Интерфейс 3Ds max'),
        KeyboardButton('Базовые моменты 3Ds max'),
        KeyboardButton('Вернуться в главное меню')
    )
    return keyboard

def get_inline_keyboard_often_questions():
    keyboard = InlineKeyboardMarkup(row_width=3, )
    keyboard.add(
        InlineKeyboardButton('1', callback_data='question_1'),
        InlineKeyboardButton('2', callback_data='question_2'),
        InlineKeyboardButton('3', callback_data='question_3'),
        InlineKeyboardButton('4', callback_data='question_4'),
        InlineKeyboardButton('5', callback_data='question_5'),
        InlineKeyboardButton('6', callback_data='question_6'),
        InlineKeyboardButton('7', callback_data='question_7'),
        InlineKeyboardButton('8', callback_data='question_8'),
        InlineKeyboardButton('9', callback_data='question_9'),
        InlineKeyboardButton('10', callback_data='question_10'),
        InlineKeyboardButton('Дальше', callback_data='next_list')

    )
    return keyboard


