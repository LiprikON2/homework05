import telebot

access_token = open("API_KEY.txt").read()
# telebot.apihelper.proxy = {'https':'31.186.102.162:3128'}
telebot.apihelper.proxy = {'https':'54.37.131.161:3128'}


bot = telebot.TeleBot(access_token)

# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(content_types=['text'])
def echo(message: str) -> None:
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling()