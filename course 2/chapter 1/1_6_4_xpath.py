"""1.6 Поиск элементов с помощью Selenium WebDriver
На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3, при этом в
нее добавилась куча одинаковых кнопок отправки. Но сработает только кнопка с текстом "Submit", и наша задача нажать
в коде именно на неё."""
# Ответ: 25.25032067590759

from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"
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
    button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
