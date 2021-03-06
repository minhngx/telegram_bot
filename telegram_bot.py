from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup

def get_news():
    list_news=[]
    r = requests.get("https://vnexpress.net/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = new.a.get("title")
        list_news.append(newdict)

    return list_news

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def news(update: Update, context: CallbackContext) -> None:
    data = get_news()
    str1 = ""

    for item in data:
        str1 += item + "\n"
    update.message.reply_text(f'{str1}')

updater = Updater('telegram token')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('news', news))

updater.start_polling()
updater.idle()
