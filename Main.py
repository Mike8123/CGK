# Importing libraries
from bs4 import BeautifulSoup
import requests
import telebot
from telebot import apihelper
import token


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

    print(tourner, '\n'*2, question, '\n'*2, answer)

# Make dictionary
def makeDict():
    dictionary = {'tour': tourner, 'question': question, 'answ': answer}
    print(dictionary)

apihelper.proxy = {'https':'socks5://138.36.21.75:9913'}

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f'<b>Привет {message.from_user.first_name}!</b>'
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


bot.polling()


# def handleData():
#     title_re = re.compile('^([\S\s]*?)\n', flags=re.DOTALL)
#     question_re = re.compile('Вопрос 1:([\S\s]*?)\n', flags=re.DOTALL)
#     answer_re = re.compile('Ответ:([\S\s]*?)\n', flags=re.DOTALL)
#     comment_re = re.compile('Комментарий:([\S\s]*?)\n', flags=re.DOTALL)
#     source_re = re.compile('Источник(и):([\S\s]*?)\n', flags=re.DOTALL)
#     author_re = re.compile('Автор: (.+)\n')
#
#
#     regexes = {
#         'title': title_re,
#         'question': question_re,
#         'answer': answer_re,
#         'comment': comment_re,
#         'source': source_re,
#         'author': author_re,
#     }
#
#
#     def clean(rq):
#         return " ".join(rq.strip().split('\n'))
#
#
#     data = {}
#     for title, regex in regexes.items():
#         match = regex.search(rq)
#         value = ''
#         if match:
#             value = clean(match.groups()[0]) if match.groups() else value
#         data[title] = value
#
#
#     pprint(data)


# I almost got it but not completely yet
if __name__ == '__main__':
    main()