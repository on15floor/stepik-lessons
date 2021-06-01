"""2.3 Работа с окнами
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом"""
# Ответ: 28.949679195377286

from selenium import webdriver
import time
import math


def calc(var_x):
    return str(math.log(abs(12*math.sin(int(var_x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Safari()

try:
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    key = calc(x)
    input_key = browser.find_element_by_id('answer')
    input_key.send_keys(key)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
