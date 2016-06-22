from urllib.request import urlopen
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler
from telegram.error import NetworkError, Unauthorized
from datetime import datetime


def get_rate(bank, table):
    html = urlopen(bank)
    bs_html = BeautifulSoup(html.read(),'lxml')
    currency_list = bs_html.find('table', {'class': table}).findAll('td')
    currency_strip_list = []
    for currency in currency_list:
        currency_strip_list.append(currency.get_text().strip())
    return currencyStripList


def kkb(bot, update):
    a = get_rate('http://kkb.kz', 'tbl_kurs')
    bot.sendMessage(update.message.chat_id, text=datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")+'Kazkom\nВалюта ' + ' '.join(a[2:4]))
    bot.sendMessage(update.message.chat_id, text=' '.join(a[4:7])+'\n' + ' '.join(a[7:10])+'\n' + ' '.join(a[10:]))


def halyk(bot, update):
    a = get_rate('https://halykbank.kz', 'rates-1')
    bot.sendMessage(update.message.chat_id, text=datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")+'Народный Банк\nВалюта ' + ' '.join(a[1:3]))
    bot.sendMessage(update.message.chat_id, text=' '.join(a[3:6]) + '\n' + ' '.join(a[6:9]) + '\n' + ' '.join(a[9:]))


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Курсы валют банков Казахстана  Чтобы посмотреть помощь /help')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='/help  - эта помощь\n/kkb - Kazkom\n/halyk - Народный Банк')


def main():
    TOKEN = "197814627:AAEJ1fYVhxaa6LoUY78BoTA_jAuaqnuOlzY"
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add handlers for Telegram messages
    dp.add_handler(CommandHandler("kkb", kkb))
    dp.add_handler(CommandHandler("halyk", halyk))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()