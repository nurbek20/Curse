import telebot 
import pytube
import os
token='5216816504:AAGBSraLHgoFFoo4HeEWuqqWnUcqR7Bh81M'

bot = telebot.TeleBot(token=token)
url = 'https://youtu.be/leru8I80mFg'
# yt = pytube.YouTube(url).streams.filter(res='720p').first().download()
current_path = os.path.abspath(os.getcwd())+'/videos/'
# print(yt.title)
# @bot.message_handler(commands=['start'])

def send_message(message):
    bot.send_message(message.chat.id, "Я телеграмм бот")


@bot.message_handler(content_types='text')
def send(message):
    url = message.text
    bot.send_message(message.chat.id, 'video downloading...')
    pytube.YouTube(url).streams.filter(res='720p').first().download(output_path=current_path)
    video.title=pytube.YouTube(url).title+'.mp4'
    video = open(current_path+video_title, 'rb')
    bot.send_video(message.chat.id, video)
bot.infinity_polling()