"""2.2 Работа с файлами, списками и js-скриптами
В этом задании в форме регистрации требуется загрузить текстовый файл.
Напишите скрипт, который будет выполнять следующий сценарий:
Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку Submit"""
# Ответ: 28.907118804412356

from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Safari()
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '2_2_3_file.txt')

try:
    browser.get(link)
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("Smolensk")
    file = browser.find_element_by_id('file')
    file.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
