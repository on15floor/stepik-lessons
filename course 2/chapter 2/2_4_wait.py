"""2.4 Настройка ожиданий
Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более
высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
"""
# Ответ: 28.99383016329745

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(var_x):
    return str(math.log(abs(12*math.sin(int(var_x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Safari()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

try:
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    button = browser.find_element_by_id('book')
    button.click()
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    key = calc(x)
    input_key = browser.find_element_by_id('answer')
    input_key.send_keys(key)
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
