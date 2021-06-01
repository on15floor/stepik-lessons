# 3.3 Обзорно об интернете: http-запросы, html-страницы и requests
##############################
# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с
# дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход
# и из C в B можно перейти за один переход.
#
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
#
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.
import requests
import re


def get_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        links = re.findall(r'<a.*href=\"(.*)\".*>', response.text)
        return links
    return []


def check(url_a, url_b):
    for link in get_links(url_a):
        if url_b in get_links(link):
            print('Yes')
            return
    print('No')
    return


a = input()
b = input()
check(a, b)
