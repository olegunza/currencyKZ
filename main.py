from urllib.request import urlopen
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler
from telegram.error import NetworkError, Unauthorized
import logging


def get_kkb():
    html = urlopen('http://kkb.kz')
    bsHtml = BeautifulSoup(html.read(),'lxml')
    currencyList = bsHtml.find('table', {'class':'tbl_kurs'}).findAll('td')
    currencyStripList = []
    for currency in currencyList:
        currencyStripList.append(currency.get_text())
    return currencyStripList


def kkb(bot, update):
    a = get_kkb()
    bot.sendMessage(update.message.chat_id, text='Kazkom'+'\n' + 'Валюта ' + ' '.join(a[2:4]))
    bot.sendMessage(update.message.chat_id, text=' '.join(a[4:7])+'\n' + ' '.join(a[7:10])+'\n' + ' '.join(a[10:]))


def main():
    TOKEN = "197814627:AAEJ1fYVhxaa6LoUY78BoTA_jAuaqnuOlzY"
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add handlers for Telegram messages
    dp.add_handler(CommandHandler("kkb", kkb))


    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()