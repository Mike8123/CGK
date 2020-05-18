# Importing libraries
from bs4 import BeautifulSoup
import requests

# Requesting html-page from the url
def get_html(url):
    result = requests.get(url)
    return result.text

# Receiving data from html-page
def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    random_qustion1 = soup.find('div', {'class' : 'random_question'})
    print(random_qustion1.text)

# Main function which inicialize other functions
def main():
    html = get_html('https://db.chgk.info/random')
    get_data(html)
    gen_dic()

# Generation dictionary with placeholders
def gen_dic():
    dic1 = {
        'Турнир' : 'Название турнира',
        'Вопрос' : 'Текст вопроса',
        'Ответ' : 'Текст ответа',
        'Комментарий' : 'Комментарий к вопросу',
        'Источник' : 'Информация об источнике вопроса',
        'Автор' : 'Автор вопроса'
    }
    print(dic1.get('Вопрос'))
    print(dic1.get('Ответ'))

# Fuck, I almost don't know about anything of this
if __name__ == '__main__':
    main()