# 2.2 Работа с кодом: модули и импорт
##############################
# Алиса владеет интересной информацией, которую хочет заполучить Боб.
# Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
# У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.
#
# Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой
# из паролей ему нужен. Помогите ему решить эту проблему.
#
# Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
# Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода
# simplecrypt.encrypt.
#
# Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей
# служит ключом для расшифровки файла с интересной информацией.
#
# Ответом для данной задачи служит расшифрованная интересная информация Алисы.

import simplecrypt
import requests


response = requests.get('https://stepik.org/media/attachments/lesson/24466/passwords.txt')
passwords = response.text.split('\n')

with open('encrypted.bin', 'rb') as inp:
    encrypted = inp.read()

for password in passwords:
    password.strip()
    try:
        print(simplecrypt.decrypt(password, encrypted).decode('utf8'))
    except simplecrypt.DecryptionException:
        print(password, 'is wrong')
    else:
        print(password, 'is correct')