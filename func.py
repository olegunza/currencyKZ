from urllib.request import urlopen
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler
from telegram.error import NetworkError, Unauthorized
import logging


def get_halyk():
    html = urlopen('https://halykbank.kz')
    bsHtml = BeautifulSoup(html.read(),'lxml')
    currencyList = bsHtml.find('table', {'class':'rates-1'}).findAll('td')
    currencyStripList = []
    for currency in currencyList:
        currencyStripList.append(currency.get_text().strip())
    print (currencyStripList)
    #return currencyStripList

if __name__ == '__main__':
    get_halyk()