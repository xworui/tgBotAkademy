import keyboards
from config import bot
from telebot.types import Message, CallbackQuery
# from random import randint
# from functions import handle_name, play_command, wikiz

often_questions = ('1. Вопросссссссссссссссссссссссссссссссссссссссссссссссссссссс\n'
                   '2. Вопрос\n'
                   '3. Вопрос\n'
                   '4. Вопрос\n'
                   '5. Вопрос\n'
                   '6. Вопрос\n'
                   '7. Вопрос\n'
                   '8. Вопрос\n'
                   '9. Вопрос\n'
                   '10. Вопрос\n'
                   '1/10 страница')

@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.send_message(message.chat.id, 'Добро пожаловать в чат-бот помощника по 3Ds max', reply_markup=keyboards.get_main_keyboard())


@bot.message_handler(content_types=['text'])
def func(message: Message):
    if (message.text == "Задать доп вопрос"):
        bot.send_message(message.chat.id, 'Слушай ваш вопрос: ')

    elif (message.text == "3Ds max"):
        bot.send_message(message.chat.id, 'Меню', reply_markup=keyboards.get_main_3dmax_keyboard())

    elif (message.text == "Вернуться в главное меню"):
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=keyboards.get_main_keyboard())

    elif (message.text == 'Часто задаваемые вопросы'):
        bot.send_message(message.chat.id, often_questions, reply_markup=keyboards.get_inline_keyboard_often_questions())

@bot.callback_query_handler(func=lambda call : True)
def handle_inline_button_click(call: CallbackQuery):
    data = call.data
    if data == 'question_1':
        bot.send_message(call.message.chat.id, 'Ответ на 1 вопрос')
    elif data == 'question_2':
        bot.send_message(call.message.chat.id, 'Ответ на 2 вопрос')
    elif data == 'question_3':
        bot.send_message(call.message.chat.id, 'Ответ на 3 вопрос')
    elif data == 'question_4':
        bot.send_message(call.message.chat.id, 'Ответ на 4 вопрос')
    elif data == 'question_5':
        bot.send_message(call.message.chat.id, 'Ответ на 5 вопрос')
    elif data == 'question_6':
        bot.send_message(call.message.chat.id, 'Ответ на 6 вопрос')
    elif data == 'question_7':
        bot.send_message(call.message.chat.id, 'Ответ на 7 вопрос')
    elif data == 'question_8':
        bot.send_message(call.message.chat.id, 'Ответ на 8 вопрос')
    elif data == 'question_9':
        bot.send_message(call.message.chat.id, 'Ответ на 9 вопрос')
    elif data == 'question_10':
        bot.send_message(call.message.chat.id, 'Ответ на 10 вопрос')
    elif data == 'next_list':
        bot.send_message(call.message.chat.id, 'Типо некст страница')
    bot.answer_callback_query(call.id)

bot.polling(none_stop=True)