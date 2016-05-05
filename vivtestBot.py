# TODO : 1. Use WebHook to host bot on Heroku  2. If image is uploaded to Bot, Give its tinyurl For Download.
# For Making your OWN BOT. REFER : https://github.com/nickoala/telepot OR Feel free to ping me.

from pprint import pprint
import telepot
import time
import random
import hashlib
from pytube import YouTube
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import os
import telegram

TOKEN = "TOKEN_GENERATED_FROM_BOT_FATHER"
SUPER_BASE_URL = "https://www.youtube.com"
BASE_QUERY = 'https://www.youtube.com/results?search_query='
DEFAULT_MESSAGE = "Didn`t recognise this stuff currently, Try in FUTURE "+telegram.Emoji.FACE_WITH_STUCK_OUT_TONGUE_AND_WINKING_EYE
WELCOME_MESSAGE = "Hey there!\nFor now I give only Videos, so type video <title of video> and i will send it to you."+telegram.Emoji.DRAGON

def getRandomId():
    return hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()[:8]


def handle(msg):
    username = msg['from']['first_name']
    chat_id = msg['from']['id']
    base_msg_text = str(msg['text']).split(' ', 1)
    if base_msg_text[0].lower() == 'video':
        title = base_msg_text[1]
        ext = getVideo(title, chat_id, username)
        sendVideo(msg, ext, title)
    elif base_msg_text[0].lower() == '/start':
        bot.sendMessage(chat_id, WELCOME_MESSAGE)
    else:
        bot.sendMessage(chat_id, DEFAULT_MESSAGE)

    pprint(msg)


def sendVideo(msg, ext, title):
    chat_id = msg['from']['id']
    bot.sendChatAction(chat_id, 'upload_video')
    #bot.sendMessage(chat_id, 'Would take some time, Net is slow :p \nDo something else till i get this done.')
    vid = open('/home/viveksb007/Desktop/telegramtemp/videos/' + title + '.' + ext, 'rb')
    print("Sending Video ...")
    bot.sendVideo(chat_id, vid)
    bot.sendMessage(chat_id, 'Enjoy '+telegram.Emoji.SMILING_FACE_WITH_OPEN_MOUTH)
    print("Video Send :)")


def getVideo(title, chat_id, username):
    BASE_TAG = title.replace(' ', '+')
    QUERY = BASE_QUERY + BASE_TAG
    response = requests.get(QUERY)
    soup = BeautifulSoup(response.text, "html.parser")
    links_list = []
    for i in soup.find_all('a', attrs={'rel': 'spf-prefetch'}):
        print(i['href'])
        links_list.append(i['href'])
    url_to_download = SUPER_BASE_URL + links_list[0]
    yt = YouTube(url_to_download)
    bot.sendMessage(chat_id, "Hey " + username + "\nTitle : " + yt.filename + "\nis on its way ..")
    yt.set_filename(title)

    ## LOW QUALITY DUE TO SLOW NET
    #zero_choice = yt.filter(extension='3gp', resolution='144p')

    first_choice = yt.filter(extension='mp4', resolution='240p')
    second_choice = yt.filter(extension='flv', resolution='240p')
    if first_choice == []:
        vid = yt.get(extension='flv', resolution='240p')
        ext = 'flv'
    else:
        vid = yt.get(extension='mp4', resolution='240p')
        ext = 'mp4'


    #vid = yt.get(extension='3gp', resolution='144p')
    #ext = '3gp'

    print("Downloading ...")
    if not os.path.exists('/home/viveksb007/Desktop/telegramtemp/videos/'+title+'.'+ext):
        vid.download('/home/viveksb007/Desktop/telegramtemp/videos/')
        print("Download Completed")
    else:
        print("Already Downloaded")
    return ext


if __name__ == '__main__':
    bot = telepot.Bot(TOKEN)
    bot.message_loop(handle)
    while True:
        # FOR Infinite Time
        time.sleep(10)

