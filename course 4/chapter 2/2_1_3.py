"""2. Повторяем основные конструкции языка Python. Часть 1.
Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том
числе пробел) стоит 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.
"""
s = input()
coins = len(s) * 60
print(f'{coins // 100} р. {coins % 100} коп.')