# 3.5 API
##############################
# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
#
# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт
# об этом числе.
#
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
#
# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
#
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true
import requests


def check_number(number):
    params = {'default': 'Boring number is boring', 'json': True}
    response = requests.get(f'http://numbersapi.com/{number}/math', params)
    data = response.json()
    if 'boring' in data['text']:
        return 'Boring'
    else:
        return 'Interesting'


with open('dataset_24476_3.txt') as f:
    for n in f:
        print(check_number(n.strip()))
