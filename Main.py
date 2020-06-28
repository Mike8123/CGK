# Importing libraries
from bs4 import BeautifulSoup
import requests
import telebot
from telebot import types
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

        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Ответ", callback_data='answerButton')

        markup.add(item1)

        bot.send_message(message.chat.id, Qest, parse_mode='html', reply_markup=markup)

    except:
        # bot.send_message(message.chat.id, 'Упс... Попробуй другой вопрос((', parse_mode='html')
        quest(message)

# Answer message handler
@bot.message_handler(commands=['answer'])
def a(message):
    try:
        global Ans

        Ans = {dic.get('a')}
        bot.send_message(message.chat.id, Ans, parse_mode='html')

    except:
        bot.send_message(message.chat.id, 'Сначала я задам тебе вопрос)', parse_mode='html')
        quest(message)


# Tour message handler
@bot.message_handler(commands=['tour'])
def tour(message):
    try:
        tourn = {dic.get('t')}
        bot.send_message(message.chat.id, tourn, parse_mode='html')

    except:
        bot.send_message(message.chat.id, 'Сначала я задам тебе вопрос)', parse_mode='html')
        quest(message)


# Add inline button which display answer alert
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'answerButton':
                user = call.from_user.first_name
                cheater = f'{user} подсмотрел ответ 😉'
                bot.send_message(call.message.chat.id, cheater)


            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=answer)

    except Exception as e:
        print(repr(e))


# Don't stop dude
bot.polling(none_stop=True)