"""2.3 Работа с окнами
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver
на новую вкладку и решить в ней задачу. Сценарий для реализации выглядит так:
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ"""
# Ответ: 28.95054735510924

from selenium import webdriver
import time
import math


def calc(var_x):
    return str(math.log(abs(12*math.sin(int(var_x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Safari()

try:
    browser.get(link)
    button = browser.find_element_by_css_selector("button.trollface")
    button.click()
    new_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
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
