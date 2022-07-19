# import psycopg2
# connect = psycopg2.connect(
#     host= "localhost", 
#     port="5432", 
#     database="postgres", 
#     user="postgres", 
#     password="postgres"
# ) pip install pyTelegramBotAPI    python tele.py    pip install googletrans==4.0.0-rc1
# source venv/bin/activate 
# deactivate venv/bin/activate 
# python -m pip install Django  
# python manage.py runserver 
# python manage.py startapp main
# python3 -m  venv venv 
# source venv/bin/activate
# pip install googletrans==4.0.0-rc1
# pip install googletrans
# pip install requests  pip install -r requirements.txt
# deactivate venv/bin/activate   
# pip freeze > requirements.txt  
# touch .gitignore
# django-admin startproject mysitee   
# django-admin startproject myfirst
# python -m django --version
# git commit -m "created app:main, connected templates and static files"
# python manage.py createsuperuser
# python3 manage.py migrate 
# python3 manage.py makemigrations 
# pip install pillow 
# django-admin startapp core


# import telebot
# bot = telebot.TeleBot('5155201521:AAFCtvu3L2JKYvUZ8eXLyUIko0BYqzE2OkM')

# @bot.message_handler(commands=['start', 'hi'])
# def send_welcome(message):
#     bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text.lower() == "Привет":
#         bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.chat.id, "Напиши привет")
#     elif message.text.lower() == 'как дела?':
#         bot.send_message(message.chat.id, 'хорошо')
#     elif message.text.lower() == 'создатель':
#         bot.send_message(message.chat.id, '@apex_emir')
#     elif message.text.lower() == 'python':
#         bot.send_message(message.chat.id, 'Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ.')
#     elif message.text.lower() == 'audio':
#         bot.send_audio(message.chat.id, 'https://muzon-music.com/public/vk.play.php?id=371745462_456493882&vk_hash=764_64a8d8c94dffc2962a&hash=40026f7efb4b1b400bee92c8183becbe&a=AC/DC&t=Thunderstruck&name=ac-dc_thunderstruck')
#     elif message.text.lower() == 'фото':
#         bot.send_photo(message.chat.id, 'https://www.google.com/imgres?imgurl=https%3A%2F%2Favatanplus.ru%2Ffiles%2Fresources%2Foriginal%2F5c5e490148135168d04d2d0f.png&imgrefurl=https%3A%2F%2Favatanplus.com%2Fdetail%2Fresource-3856280&tbnid=vT6Yy6dLXGzf0M&vet=12ahUKEwjtlK762LzxAhVCzyoKHdRxCMkQMyglegUIARCdAg..i&docid=OV0rx842PxbiuM&w=550&h=541&q=png%20%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8&client=ubuntu&ved=2ahUKEwjtlK762LzxAhVCzyoKHdRxCMkQMyglegUIARCdAg')
#     elif message.text.lower() == 'аман':
#         bot.send_photo(message.chat.id, 'https://n1s1.hsmedia.ru/70/03/37/700337f23cd273503d1df498e073f644/500x361_0xac120003_13762508961615799384.jpg')
#     elif message.text.lower() == 'стикер':
#         bot.send_sticker(message.chat.id, 'https://tlgrm.ru/_/stickers/73a/aed/73aaedd6-70a6-40f1-ae0d-1c0ed846a5b3/1.webp')
#     elif message.text.lower() == 'gif':
#         bot.send_animation(message.chat.id, 'https://giphy.com/gifs/angrybirds-angry-birds-leonard-movie-l41Ys1fQky5raqvMQ')
#     else:
#         bot.send_message(message.chat.id, 'Не понимаю, что это значит.')

# bot.polling()



# import telebot
# import requests
# import json
# import pytube
# import calendar
# import time

# bot = telebot.TeleBot('1897153800:AAG6W-C8swxBCt9R_eoBaYQOcOpYWqGVQu8')

# weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=fa0c69065a227aae0ae1081d5953bcfa&units=metric'

# covid_url = 'https://covid-api.mmediagroup.fr/v1/cases?country={country}'

# @bot.message_handler(commands=['start', 'hi'])
# def welcome(message):
#     bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name} ')

# @bot.message_handler(content_types=['text']) 
# def get_text_messages(message):

#     if message.text == 'привет':
#         bot.send_message(message.chat.id, f'привет {message.from_user.first_name}')
#     elif message.text.lower() == '/help':
#         bot.send_message(message.chat.id, '/help погода, /help cord, /help hello, /help video')
#     elif message.text.lower() == '/help погода':
#         bot.send_message(message.chat.id,'если хочешь узнать погоду пример: погода ru moscow')
#     elif message.text.lower() == '/help cord':
#         bot.send_message(message.chat.id,'если хочешь узнать кординаты пример: cord ru moscow')
#     elif message.text.lower() == '/help hello':
#         bot.send_message(message.chat.id,'напиши привет!')
#     elif message.text.lower() == '/help video':
#         bot.send_message(message.chat.id,' вставте ссылку видео из youtube!')
#     elif message.text.lower() == 'спасибо':
#         bot.send_animation(message.chat.id,'https://media.giphy.com/media/zzALYeLqMLDa6PEV2C/giphy.gif')
#     elif message.text.split(' ')[0] == 'погода':
#         textsplitted = message.text.lower().split(' ')
#         city = textsplitted[2]
#         country = textsplitted[1]
#         w_final_url = weather_url.format(city=city, country=country)
#         response = requests.get(w_final_url)
#         pog_json  = response.json()
#         country = pog_json['sys']['country']
#         gor = pog_json['name']
#         temp = pog_json['main']['temp']
#         feel = pog_json['main']['feels_like']
#         wind = pog_json['wind']['speed']
#         bot.send_message(message.chat.id,f'код страны { country }')
#         bot.send_message(message.chat.id,f'погода в городе { gor }')
#         bot.send_message(message.chat.id,f'{ temp } градусов')
#         bot.send_message(message.chat.id,f'ошушается как { feel }')
#         bot.send_message(message.chat.id,f'скорость ветра { wind } км/ч')
    
#     elif message.text.split(' ')[0] == 'cord':
#         textsplitted = message.text.lower().split(' ')
#         city = textsplitted[2]
#         country = textsplitted[1]
#         w_final_url = weather_url.format(city=city, country=country)
#         response = requests.get(w_final_url)
#         cord_json  = response.json()
#         lat = cord_json['coord']['lat'] 
#         lon = cord_json['coord']['lon'] 
#         bot.send_message(message.chat.id,f' широта : { lat }')
#         bot.send_message(message.chat.id,f'долгота : { lon }')
    
#     elif message.text.split(' ')[0].lower() == 'covid':
#         text = message.text.split(' ')
#         country_code = text[1]
#         wcovid_url = covid_url.format( country = country_code )
#         res = requests.get(wcovid_url)
#         re_json  = res.json()

#         con = re_json['All']['confirmed']
#         de = re_json['All']['deaths']
#         re = re_json['All']['recovered']
#         co = re_json['All']['country']
#         po = re_json['All']['population']

#         bot.send_message(message.chat.id, f'🤒 { con }')
#         bot.send_message(message.chat.id, f'💀 { de }')
#         bot.send_message(message.chat.id, f'😷 { re }')
#         bot.send_message(message.chat.id, f'страна :{ co }')
#         bot.send_message(message.chat.id,f'Население : { po }')

#     else:
#         bot.send_message(message.chat.id, 'я не понимаю что это значит напишите /help')

# print('бот работает.....')
# bot.polling()


  
# import telebot
# import requests
# import json


# bot = telebot.TeleBot('1897153800:AAG6W-C8swxBCt9R_eoBaYQOcOpYWqGVQu8')

# day_url = 'https://holidays.abstractapi.com/v1/?api_key=2872cf258d92486696bc58d963af2797&country={country}&year=2021&month={month}&day={day}'

# @bot.message_handler(commands=['start', 'hi'])
# def welcome(message):
#     bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name} ')
#     bot.reply_to(message, 'пример команды: дата us 2 12')


# @bot.message_handler(content_types=['text']) 
# def get_text_messages(message):

#     if message.text == 'привет':
#         bot.send_message(message.chat.id, f'привет {message.from_user.first_name}')
#     elif message.text.split(' ')[0].lower() == 'день':
#         text = message.text.split(' ')
#         country = text[1]
#         month_code = text[2]
#         day_code = text[3]

#         day_fi = day_url.format(country = country,month = month_code, day = day_code)
#         response = requests.get(day_fi)
#         popjson = response.json()

#         n = popjson[0]['name']
#         c = popjson[0]['country']
#         location = popjson[0]['location']
#         week = popjson[0]['week_day']
#         date = popjson[0]['date']

#         bot.send_message(message.chat.id,f'название праздника:{n}')
#         bot.send_message(message.chat.id,f'дата {date} ')
#         bot.send_message(message.chat.id,f'город:{c}')
#         bot.send_message(message.chat.id,f'локация:{location}')
#         bot.send_message(message.chat.id,f'день недели:{week}')
    
#     else:
#         bot.send_message(message.chat.id, '?')

# print('бот работает.....')
# bot.polling()

# import telebot
# import requests
# import json
# import pytube
# import calendar
# import time

# bot = telebot.TeleBot('1730611798:AAHYvIqkWX5lZGwy-Hsg7DapH3BUwRCdZg4')

# @bot.message_handler(commands=['start', 'hi'])
# def welcome(message):
#     bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name} ')

# @bot.message_handler(content_types=['text']) 
# def get_text_messages(message):

#     if message.text.find('youtube.com/watch?v='):
#         url = message.text
#         youtube = pytube.YouTube(url)
#         video = youtube.streams.get_by_resolution('360p')
#         bot.send_message(message.chat.id, 'мы качаем видео подождите...')
#         filename = str(calendar.timegm(time.gmtime()))
#         video.download(
#             filename = filename,
#             output_path = '/home/neo-d/videos'
#         )
#         bot.send_message(message.chat.id, 'мы скачали ваше видео вот держите')
#         filepath = '/home/neo-d/videos/{filename}.{ext}'.format(
#             filename = filename,
#             ext = 'mp4'
#         )
#         downloaded_video = open(filepath, 'rb')
#         bot.send_video(message.chat.id, downloaded_video)

# print('бот работает.....')
# bot.polling()


# [
#   {
#     "name": "New Year",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "01/01/2021",
#     "date_year": "2021",
#     "date_month": "01",
#     "date_day": "01",
#     "week_day": "Friday"
#   },
#   {
#     "name": "Orthodox Christmas Day",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "01/07/2021",
#     "date_year": "2021",
#     "date_month": "01",
#     "date_day": "07",
#     "week_day": "Thursday"
#   },
#   {
#     "name": "Defender of the Fatherland Day",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "02/23/2021",
#     "date_year": "2021",
#     "date_month": "02",
#     "date_day": "23",
#     "week_day": "Tuesday"
#   },
#   {
#     "name": "International Women's Day",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "03/08/2021",
#     "date_year": "2021",
#     "date_month": "03",
#     "date_day": "08",
#     "week_day": "Monday"
#   },
#   {
#     "name": "March Equinox",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "Seasonal",
#     "date": "03/20/2021",
#     "date_year": "2021",
#     "date_month": "03",
#     "date_day": "20",
#     "week_day": "Saturday"
#   },
#   {
#     "name": "National \"Nooruz\"",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "03/21/2021",
#     "date_year": "2021",
#     "date_month": "03",
#     "date_day": "21",
#     "week_day": "Sunday"
#   },
#   {
#     "name": "National \"Nooruz\"",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "03/22/2021",
#     "date_year": "2021",
#     "date_month": "03",
#     "date_day": "22",
#     "week_day": "Monday"
#   },
#   {
#     "name": "April People's Revolution Day",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "04/07/2021",
#     "date_year": "2021",
#     "date_month": "04",
#     "date_day": "07",
#     "week_day": "Wednesday"
#   },
#   {
#     "name": "May Day",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "05/01/2021",
#     "date_year": "2021",
#     "date_month": "05",
#     "date_day": "01",
#     "week_day": "Saturday"
#   },
#   {
#     "name": "May Day",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "05/03/2021",
#     "date_year": "2021",
#     "date_month": "05",
#     "date_day": "03",
#     "week_day": "Monday"
#   },
#   {
#     "name": "Constitution Day of the Kyrgyz Republic",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "05/05/2021",
#     "date_year": "2021",
#     "date_month": "05",
#     "date_day": "05",
#     "week_day": "Wednesday"
#   },
#   {
#     "name": "Victory Day",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "05/09/2021",
#     "date_year": "2021",
#     "date_month": "05",
#     "date_day": "09",
#     "week_day": "Sunday"
#   },
#   {
#     "name": "Victory Day",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "05/10/2021",
#     "date_year": "2021",
#     "date_month": "05",
#     "date_day": "10",
#     "week_day": "Monday"
#   },
#   {
#     "name": "Orozo Ait",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "05/13/2021",
#     "date_year": "2021",
#     "date_month": "05",
#     "date_day": "13",
#     "week_day": "Thursday"
#   },
#   {
#     "name": "June Solstice",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "Seasonal",
#     "date": "06/21/2021",
#     "date_year": "2021",
#     "date_month": "06",
#     "date_day": "21",
#     "week_day": "Monday"
#   },
#   {
#     "name": "Kurman Ait",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "07/20/2021",
#     "date_year": "2021",
#     "date_month": "07",
#     "date_day": "20",
#     "week_day": "Tuesday"
#   },
#   {
#     "name": "Independence Day of the Kyrgyz Republic",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "08/31/2021",
#     "date_year": "2021",
#     "date_month": "08",
#     "date_day": "31",
#     "week_day": "Tuesday"
#   },
#   {
#     "name": "September Equinox",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "Seasonal",
#     "date": "09/23/2021",
#     "date_year": "2021",
#     "date_month": "09",
#     "date_day": "23",
#     "week_day": "Thursday"
#   },
#   {
#     "name": "Day of the Great October Socialist Revolution",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "11/07/2021",
#     "date_year": "2021",
#     "date_month": "11",
#     "date_day": "07",
#     "week_day": "Sunday"
#   },
#   {
#     "name": "Day of the Great October Socialist Revolution",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "National",
#     "date": "11/08/2021",
#     "date_year": "2021",
#     "date_month": "11",
#     "date_day": "08",
#     "week_day": "Monday"
#   },
#   {
#     "name": "December Solstice",
#     "name_local": "",
#     "language": "",
#     "description": "",
#     "country": "KG",
#     "location": "Kyrgyzstan",
#     "type": "Seasonal",
#     "date": "12/21/2021",
#     "date_year": "2021",
#     "date_month": "12",
#     "date_day": "21",
#     "week_day": "Tuesday"
#   }
# ]