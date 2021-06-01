"""1.6 Поиск элементов с помощью Selenium WebDriver
На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней."""
# Ответ: 25.1962528259999

from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Safari()
key = str(math.ceil(math.pow(math.pi, math.e)*10000))

value1 = 'input'
value2 = 'last_name'
value3 = 'form-control.city'
value4 = 'country'

try:
    browser.get(link)
    link = browser.find_element_by_link_text(key)
    link.click()
    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
