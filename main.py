import telebot

bot = telebot.TeleBot('6736084219:AAGWCFhvNuyTUe8VWUxYC2uhCZCkWarN1PI')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Сообщение')


@bot.message_handler(commands=['fly'])
def main(message):
    bot.send_message(message.chat.id, 'лети /nлети!')


bot.infinity_polling()
