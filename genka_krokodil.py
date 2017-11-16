# -*- coding: utf-8 -*-
import config #подключаем файл с настройками
import telebot #для работы с Telegram API
import os # для работы с операционной системой
import requests
import bs4
from telebot import types

bot = telebot.TeleBot(config.token) #Подключаемся к боту с помощью Telegram API
directory_music = config.directory_music  #Директория,в который будут лежать файлы с музыкой
directory_foto = config.directory_foto  #Директория,в которой будут лежать фотографии
directory_document = config.directory_document  #Директория,в которой будут лежать документы

#def music_array():
music_list = [] #Массив,содержащий в себе список всех песен из directory_music
for i in os.listdir(directory_music): #Получаем название песен из directory_music
    music_list.append(i) #Добавляем название в массив

music_del_list = [] #Массив,содержащий в себе список всех песен из directory_music
for i in os.listdir(directory_music): #Получаем название песен из directory_music
    music_del_list.append('del_'+i) #Добавляем название в массив и добавляем ей  заголовок del_

#def doc_array():
documents_list = [] #Массив,содержащий в себе список всех документов из directory_document
for i in os.listdir(directory_document): #Получаем название документов из directory_document
    documents_list.append(i) #Добавляем название в массив

documents_del_list = [] #Массив,содержащий в себе список всех документов из directory_document
for i in os.listdir(directory_document): #Получаем название документов из directory_document
    documents_del_list.append('del_'+i) ##Добавляем название в массив и добавляем ей  заголовок del_


hello = ('привет','приветик','здраствуй','здорова','здарова','шалом','hi','hello')
bay = ('пока','прощай','до завтра','до свидания генка','bay','досвидули')
sleep = ('спокойной ночи','сладких снов')
dela = ('как дела','как дела?','как дела?)','как делишки')
rfpl = ('скинь таблицу рфпл','генка скинь таблицу рфпл','рфпл')
fclm = ('новости про локо','скинь новости про локо','что там в локо','новости локо','как там локо')
pogoda = ('как погода', 'как погода?','как там погода?','как там погода','kak pogoda', 'что там с погодой?' , 'погода')
zanytie = ('что делаешь что делаешь? ','что делаешь)' ,'что делаешь?)' ,'генка,что делаешь?')
cool = ('клево', 'здорово', 'класно', 'здорово)', 'клево)', 'класно)','кайфово')
music = ('список музыки','какие песни у тебя есть','какая музыка у тебя есть','скачать песню')
table_football = ('таблицы чемпионатов по футболу','таблица чемпионатов по футболу','таблица по футболу','футбольная таблица','скинь таблицу')


# Подпрограмма, формирующая стартовую клавиатуру
def start_keyboard(message,s):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('Новости про локо', 'Таблицы чемпионатов по футболу')
    keyboard.row('Музыка', 'Документы')
    bot.send_message(message.chat.id,s, reply_markup=keyboard)

# Подпрограмма формирования клавиатуры при нажатии в главном меню  кнопки "Музыка"
def music_add_keyboard(message,s):
    music_keyboard = types.ReplyKeyboardMarkup()
    music_keyboard.row('Скачать песню')
    music_keyboard.row('Удалить песню')
    music_keyboard.row('Добавить песню')
    music_keyboard.row('Вернуться в главное меню')
    bot.send_message(message.chat.id,s, reply_markup=music_keyboard)

# Подпрограмма формирования клавиатуры при нажатии в главном меню  кнопки "Документы"
def doc_add_keyboard(message,s):
    doc_keyboard = types.ReplyKeyboardMarkup()
    doc_keyboard.row('Скачать файл')
    doc_keyboard.row('Удалить файл')
    doc_keyboard.row('Добавить файл')
    doc_keyboard.row('Вернуться в главное меню')
    bot.send_message(message.chat.id,s, reply_markup=doc_keyboard)

# Подпрограмма, формирующая клавиатуру, содержащую список музыки из папки directory_music и добавляет заголовок del_
def music_del_keyboard(message,s):
    music_keyboard = types.ReplyKeyboardMarkup()
    for i in os.listdir(directory_music):
        music_keyboard.row('del_'+i)
    music_keyboard.row('Вернуться в раздел Музыка')
    music_keyboard.row('Вернуться в главное меню')
    bot.send_message(message.chat.id, s, reply_markup=music_keyboard)

# Подпрограмма, формирующая клавиатуру, содержащую список файлов из папки directory_document и добавляет заголовок del_
def doc_list_keyboard(message,s):
    doc_keyboard = types.ReplyKeyboardMarkup()
    for i in os.listdir(directory_document):
        doc_keyboard.row('del_'+i)
    doc_keyboard.row('Вернуться в раздел Документы')
    doc_keyboard.row('Вернуться в главное меню')
    bot.send_message(message.chat.id, s, reply_markup=doc_keyboard)

# Подпрограмма, формирующая клавиатуру, содержащую список файлов из папки directory_document
def download_doc_keyboard(message,s):
    doc_keyboard = types.ReplyKeyboardMarkup()
    for i in os.listdir(directory_document):
        doc_keyboard.row(i)
    doc_keyboard.row('Вернуться в раздел Документы')
    doc_keyboard.row('Вернуться в главное меню')
    bot.send_message(message.chat.id,s, reply_markup=doc_keyboard)

#Ведем логи
def log(message,answer):
    print("\n---------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текс = {3}".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print("Ответ бота -", answer)

#Действия, которые будут выполнены при вводе команды /start
@bot.message_handler(commands=['start'])
def send_start(message):
    start_keyboard(message,"Привет!Меня зовут Геннадий Крокодильев.Чем я могу помочь?")

#Действия, которые будут выполнены при отправке боту документа
@bot.message_handler(content_types=['document'])
def handle_document(message):
    try:
        chat_id = message.chat.id
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = directory_document + message.document.file_name;
        with open(src, 'wb') as new_file:
             new_file.write(downloaded_file)
        bot.reply_to(message, "Пожалуй, я сохраню это")
        doc_add_keyboard(message,"Ты находишься в разделе Документы")
    except Exception as e:
           bot.reply_to(message, e)

#Действия, которые будут выполнены при отправке боту музыкального файла
@bot.message_handler(content_types=['audio'])
def handle_music(message):
    try:
        chat_id = message.chat.id
        file_info = bot.get_file(message.audio.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        print (file_info.file_path)
        src='/home/telegram/'+file_info.file_path;
        with open(src, 'wb') as new_file:
             new_file.write(downloaded_file)
        bot.reply_to(message,"Аудио добавлено" )
        music_add_keyboard(message,"Ты находишься в разделе Музыка")
    except Exception as e:
           bot.reply_to(message,e )

#Действия, которые будут выполнены при отправке боту фотографии
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        chat_id = message.chat.id
        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = '/home/telegram/'+file_info.file_path;
        with open(src, 'wb') as new_file:
             new_file.write(downloaded_file)
        bot.reply_to(message, "Пожалуй, я сохраню это")
    except Exception as e:
           bot.reply_to(message, e)


#Действия, которые будут выполнены при отправке текстового сообщения боту
@bot.message_handler(content_types=["text"])
def send_text(message):
    try:
        text = message.text.lower() #Присваеваем переменной "text" текст сообщения в нижнем регистре

        if text in hello:
             bot.send_message(message.chat.id,'Привет,'+message.from_user.first_name+')') #message.from_user.first_name - имя отправителя сообщения

        elif text in bay:
             bot.send_message(message.chat.id,'Досвидули)')

        elif text in sleep:
             bot.send_message(message.chat.id,'Сладких снов)')

        elif text in dela:
             bot.send_message(message.chat.id,'Отлично')

# Формирует новости про ФК Локомотив Москва
        elif text in fclm:
             try:
                 URL = 'https://lokomotiv.info/'
                 site=requests.get(URL)
                 b=bs4.BeautifulSoup(site.text, "html.parser")
                 table = b.find('table', class_='more-link')
                 result = 'Новости\n'
                 for rows in table.find_all('tr'):
                     cols=rows.find_all('td')
                     res=cols[2].a.text+' '+cols[2].a.get('href')+'\n'
                     result = result+res+'-------------------------\n'
                 bot.send_message(message.chat.id,result,parse_mode="Markdown")
             except Exception as e:
                    bot.send_message(message.chat.id, "При формировании новостей произошла ошибка")

# Формируем турнирную таблицу РФПЛ
        elif text in rfpl:
             try:
                 site=requests.get('http://rfpl.org/')
                 b=bs4.BeautifulSoup(site.text, "html.parser")
                 blok = b.find('div', class_='tournament-table tournament-table-index')
                 table = blok.find('table')
                 s1='№'+' '+'Клуб'+' '+ 'И'+' '+' О \n'
                 for rows in table.find_all('tr')[1:]:
                     cols = rows.find_all('td')
                     s=cols[0].span.text+' '+cols[2].p.text+' '+cols[3].p.text+' '+cols[8].p.text+'\n'
                     s1=s1+s
                 bot.send_message(message.chat.id,s1,parse_mode="Markdown")
             except Exception as e:
                    bot.send_message(message.chat.id, "При формировании турнирной таблицы РФПЛ произошла ошибка")

# Формируем турнирную таблицу ФНЛ
        elif text == "фнл":
             try:
                 URL = 'http://www.1fnl.ru/champioship/table/'
                 site=requests.get(URL)
                 b=bs4.BeautifulSoup(site.text, "html.parser")
                 blok = b.find('div', class_='ttable_page')
                 table = blok.find('table')
                 thead = table.find ('thead')
                 body = table.find('tbody')
                 result ='№'+' '+'Клуб'+' '+ 'И'+' '+' О \n'
                 for rows in body.find_all('tr'):
                     cols = rows.find_all('td')
                     t = cols[0].text +' '+cols[1].text+' '+cols[2].text+ ' '+cols[7].text+'\n'
                     result = result + t
                 bot.send_message(message.chat.id,result,parse_mode="Markdown")
             except Exception as e:
                    bot.send_message(message.chat.id, "При формировании турнирной таблицы ФНЛ произошла ошибка")

# Создаем кнопки клавиатуры при нажатии в главном меню  кнопки "Таблицы чемпионатов по футболу"
        elif text in table_football:
          #Создаем клавиатуру с выбором чемпионата по футболу
             football_keyboard = types.ReplyKeyboardMarkup()
             football_keyboard.row('РФПЛ')
             football_keyboard.row('ФНЛ')
             football_keyboard.row('Вернуться в главное меню')
          #Выводим сообщение и клавиатуру на экран
             bot.send_message(message.chat.id, "Какой турнир показать?", reply_markup=football_keyboard)

# Создаем кнопки клавиатуры при нажатии в главном меню  кнопки "Музыка"
        elif text == "музыка":
             s = "Что ты хочешь сделать с моим плейлистом?"
             music_add_keyboard(message,s) #Выводим кнопки с выбором действий в разделе Музыка

# Создаем кнопки клавиатуры при нажатии в меню музыка кнопки "Удалить песню"
        elif text == "удалить песню":
             s= "Какую песню нужно удалить? Небойся,что в названии песен del_ так надо)"
             music_del_keyboard(message,s)
# Удаляем выбранную песню
        elif text in music_del_list:
             try:
                 path = directory_music + text[4:] # text[4:] - удаляем 4 первых символа в переменной text
                 os.remove(path)
                 music_del_keyboard(message,"Песня успешно удалена")
             except Exception as e:
                    bot.send_message(message.chat.id, "При удалении файла произошла ошибка")

# Выводим список песен,которые есть в папке.При нажатии на песню, песня скачивается
        elif text in music:
          #Создаем клавиатуру,содержащую список песен
             music_keyboard = types.ReplyKeyboardMarkup()
             for i in os.listdir(directory_music):
                 music_keyboard.row(i)
             music_keyboard.row('Вернуться в раздел Музыка')
             music_keyboard.row('Вернуться в главное меню')
             bot.send_message(message.chat.id, "Вот мои песни", reply_markup=music_keyboard)

#Скачивание песни
        elif text in music_list:

             try:
                 audio_path = directory_music + text
                 audio = open(audio_path,'rb')
                 bot.send_audio(message.chat.id,audio,'Лови песенку')
             except Exception as e:
                    bot.send_message(message.chat.id, "При скачивании  файла произошла ошибка")

        elif text == "вернуться в раздел музыка":
             s = "Ты успешно вернулся в раздел Музыка."+"\n"+"Что ты хочешь сделать с моим плейлистом?"
             music_add_keyboard(message,s) #Выводим кнопки с выбором действий в разделе Музыка

        elif text == "добавить песню":
             bot.send_message(message.chat.id, "Ты можешь скинуть мне песню стандартными средствами Telegram")

# Создаем кнопки клавиатуры при нажатии в главном меню  кнопки "Документы"
        elif text == "документы":
             s = "Что ты хочешь сделать с моими документами?"
             doc_add_keyboard(message,s)

        elif text == "добавить файл":
             bot.send_message(message.chat.id, "Ты можешь скинуть мне документ стандартными средствами Telegram")

        elif text == "вернуться в раздел документы":
             s = "Ты успешно вернулся в раздел Документы."+"\n"+"Что ты хочешь сделать с моими документами?"
             doc_add_keyboard(message,s)

# Создаем кнопки клавиатуры при нажатии в меню документ кнопки "Удалить документ"
        elif text == "удалить файл":
             s = "Какой документ нужно удалить? Небойся,что в названии документа del_ так надо)"
             doc_list_keyboard(message,s)

# Удаляем выбранный документ
        elif text in documents_del_list:
             try:
                 path = directory_document + text[4:] # text[4:] - удаляем 4 первых символа в переменной text
                 os.remove(path)
                 doc_list_keyboard(message,"Файл успешно удален")
             except Exception as e:
                    bot.send_message(message.chat.id, "При удалении файла произошла ошибка")

# Выводим список файлов,которые есть в папке.При нажатии на файл, файл скачивается
        elif text == "скачать файл":
             s = "Вот мои документы"
             download_doc_keyboard(message,s)
#Скачивание документа
        elif text in documents_list:

             try:
                 doc_path = directory_document + text
                 doc = open(doc_path,'rb')
                 bot.send_document(message.chat.id,doc,'Лови')
             except Exception as e:
                    bot.send_message(message.chat.id, "При скачивании  файла произошла ошибка")

        elif text == "вернуться в главное меню":
             start_keyboard(message,"Вы вернулись в главное меню")

        elif text in zanytie:
             bot.send_message(message.chat.id,'Валяюсь)')

        elif text == "скинь фото" or text == "скинь фото)" or text == "скинь фотку" or text == "генка скинь фото":
             photo =open('/home/telegram/photos/genka.jpg','rb')
             bot.send_photo(message.chat.id, photo, 'Лови')

        elif text == "ты гадский" or text == "генка ты гадский" or text == "генка,ты гадский":
             bot.send_message(message.chat.id,"Сами вы гадские, ненавижу вас")

        elif text == "кто лучший футболист" or text == "кто лучший футболист?" or text == "генка кто лучший футболист":
             bot.send_message(message.chat.id,'Дзюба конечно же')

        elif text in cool:
             bot.send_message(message.chat.id,'Ага)')

        elif text == "юрий палыч всех шатал" or text == "юрий палыч шатает всех":
             photo =open('/home/telegram/photos/semin.jpg','rb')
             bot.send_photo(message.chat.id, photo,'Юрий палыч оле-оле')

        else:bot.send_message(message.chat.id,'Вы глупости пишете,я не буду с вами говорить')
    except Exception as e:
           bot.reply_to(message, e)

bot.polling()
