"""2.2 Работа с файлами, списками и js-скриптами
Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он
справился с новым заданием.
Напишите код, который реализует следующий сценарий:
Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"."""
# Ответ: 28.90485100424941

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Safari()

try:
    browser.get(link)
    num1 = browser.find_element_by_id('num1')
    var_1 = int(num1.text)
    num2 = browser.find_element_by_id('num2')
    var_2 = int(num2.text)
    key = var_1 + var_2
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(key))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
