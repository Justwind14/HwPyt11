import random
import telebot
from bs4 import BeautifulSoup as b
import requests
import lxml

"""Парсинг сайта с анекдотами"""

URL = 'https://stavropol.bankiros.ru/currency'  # от куда берем анекдоты


def parser(url):
    r = requests.get(url)  # создаем запрос
    # print(r.status_code)  #статус запроса, 200 - положительный
    soup = b(r.text, 'html.parser')  # запускаем парсер для текста
    anekdots = soup.find_all('span', class_="xxx-fs-18 xxx-text-bold xxx-text-color-success tooltip-hover")  # коллекция анекдотов
    return [c.text for c in anekdots]


# clear_anekdots = [c.text for c in anekdots] # берем только содержимое, без дива и класса


list_of_jokes = parser(URL)  # перемешиваем
print(list_of_jokes)