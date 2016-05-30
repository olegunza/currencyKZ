from urllib.request import urlopen
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler
from telegram.error import NetworkError, Unauthorized
import logging


def getKKB():
    html = urlopen('http://kkb.kz')
    bsHtml = BeautifulSoup(html.read(),'lxml')
    currencyList = bsHtml.find('table', {'class':'tbl_kurs'}).findAll('td')
    currencyStripList = []
    for currency in currencyList:
        currencyStripList.append(currency.get_text())
    return currencyStripList

def main():
    TOKEN = []
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add handlers for Telegram messages
    dp.addTelegramCommandHandler("help", help)
    dp.addTelegramCommandHandler("addcard", add_card)
    dp.addTelegramCommandHandler("removecard", remove_card)
    dp.addTelegramCommandHandler("getcards", get_cards)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()