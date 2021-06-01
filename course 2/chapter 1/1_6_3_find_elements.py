"""1.6 Поиск элементов с помощью Selenium WebDriver
В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html). С помощью неё отдел маркетинга
компании N захотел собрать подробную информацию о пользователях своего продукта. В награду за заполнение формы
становится доступен код на скидку. Но маркетологи явно переусердствовали, добавив в форму 100 обязательных полей и
ограничив время на ее заполнение. Теперь эта задача под силу только роботам."""
# Ответ: 21.207269186201056

from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Safari()

try:
    browser.get(link)
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
