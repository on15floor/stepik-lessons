"""2.1 Основные методы Selenium
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. Но теперь
значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с
изображением сундука.
Ваша программа должна:
Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit"."""
# Ответ: 28.860293519736402

from selenium import webdriver
import time
import math


def calc(var_x):
    return str(math.log(abs(12*math.sin(int(var_x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Safari()

try:
    browser.get(link)
    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute("valuex")
    key = calc(x)
    input_key = browser.find_element_by_id('answer')
    input_key.send_keys(key)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
