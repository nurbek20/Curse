import telebot

token = '5155201521:AAFCtvu3L2JKYvUZ8eXLyUIko0BYqzE2OkM'
tele = telebot.TeleBot(token=token)

@tele.message_handler(commands=['start', 'hi'])
def send_message(message):
    tele.send_message(message.chat.id, 'Hello. how are you?')


@tele.message_handler(content_types='text')
def send_message2(message):
    if message.text.lower() == 'привет':
        tele.send_message(message.chat.id, 'Привет, как ты?')    
    elif message.text.lower() == 'хорошо':
        tele.send_message(message.chat.id, 'Отлично')
    elif message.text.lower() == 'как дела?':
        tele.send_message(message.chat.id, 'хорошо')
print('БОТ работает...')
tele.infinity_polling()

