# Importing libraries
from bs4 import BeautifulSoup
import requests
import telebot
from Token import *
# from Proxy import *


# Requesting html-page from the url
def get_html(url):
    result = requests.get(url)
    return result.text


# Main function which inicialize other functions
def main():
    html = get_html('https://db.chgk.info/random')
    get_data(html)
    makeDict()


# Parsing data from html-page
def get_data(html):
    soup = BeautifulSoup(html, 'lxml')

    tour = soup.find('div', class_='random_question').find('a').text
    ques = soup.find('div', class_='random_question').find(text='Вопрос 1:').next
    answ = soup.find('div', class_='collapsible collapsed').find(text='Ответ:').next

    global tourner
    global question
    global answer

    tourner = tour
    question = ques
    answer = answ


# Make dictionary
def makeDict():
    global dic
    dic = {'t': tourner, 'q': question, 'a': answer}


# Fuck off Roskomnadzor (temporary trick)
# apihelper.proxy


# Start bot
bot = telebot.TeleBot(token)

# Start message handler
@bot.message_handler(commands=['start'])
def start(message):
    answStart = f'<b>Привет {message.from_user.first_name}!</b>'
    bot.send_message(message.chat.id, answStart, parse_mode='html')


# Question message handler
@bot.message_handler(commands=['question'])
def quest(message):
    try:
        if __name__ == '__main__':
            main()
        Qest = {dic.get('q')}
        bot.send_message(message.chat.id, Qest, parse_mode='html')
    except:
        # bot.send_message(message.chat.id, 'Упс... Попробуй другой вопрос((', parse_mode='html')
        quest(message)

# Answer message handler
@bot.message_handler(commands=['answer'])
def a(message):
    Ans = {dic.get('a')}
    bot.send_message(message.chat.id, Ans, parse_mode='html')


# Tour message handler
@bot.message_handler(commands=['tour'])
def tour(message):
    tourn = {dic.get('t')}
    bot.send_message(message.chat.id, tourn, parse_mode='html')


# Don't stop dude
bot.polling(none_stop=True)