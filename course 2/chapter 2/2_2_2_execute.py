"""2.2 Работа с файлами, списками и js-скриптами
В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который
дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:
Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit"."""
# Ответ: 28.906212227044733

from selenium import webdriver
import time
import math


def calc(var_x):
    return str(math.log(abs(12*math.sin(int(var_x)))))


link = "http://suninjuly.github.io/execute_script.html"
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
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
