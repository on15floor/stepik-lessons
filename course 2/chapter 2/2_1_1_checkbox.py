"""2.1 Основные методы Selenium
Продолжим использовать силу роботов для решения повседневных задач. На данной странице мы добавили капчу для роботов,
то есть тест, являющийся простым для компьютера, но сложным для человека.
Ваша программа должна выполнить следующие шаги:
Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit."""
# Ответ: 28.859343556220463

from selenium import webdriver
import time
import math


def calc(var_x):
    return str(math.log(abs(12*math.sin(int(var_x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Safari()

try:
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    key = calc(x)
    input_key = browser.find_element_by_id('answer')
    input_key.send_keys(key)
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
