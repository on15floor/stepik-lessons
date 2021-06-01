"""1.6 Поиск элементов с помощью Selenium WebDriver
Вам нужно открыть страницу по ссылке и заполнить форму на этой странице с помощью Selenium. Если всё сделано
правильно, то вы увидите окно с проверочным кодом. Это число вам нужно ввести в качестве ответа в этой задаче."""
# Ответ: 22.305880698316834

from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Safari()
value1 = 'input'
value2 = 'last_name'
value3 = 'form-control.city'
value4 = 'country'

try:
    browser.get(link)
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
