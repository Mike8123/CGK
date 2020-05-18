from bs4 import BeautifulSoup
import requests

def get_html(url):
    result = requests.get(url)
    return result.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    random_qustion1 = soup.find('div', {'class' : 'random_question'})
    print(random_qustion1.text)

def main():
    html = get_html('https://db.chgk.info/random')
    get_data(html)
    gen_dic()


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

if __name__ == '__main__':
    main()