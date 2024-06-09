import telebot

bot = telebot.TeleBot('7494643023:AAF6gecvemxGaAtK82lg2wcKtGs5_fGPJIc')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'На колени, перед всезнающим существом! И я позволю задать тебе вопрос!')

    bot.infinity_polling()(none_stop=True)
