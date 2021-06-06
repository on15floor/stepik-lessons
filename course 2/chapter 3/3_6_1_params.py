"""3.6 PyTest — параметризация, конфигурирование, плагины
Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать
несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать автотест со следующим
сценарием действий:
открыть страницу
ввести правильный ответ
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!" """
# Ответ: The owls are not what they seem! OvO

from selenium import webdriver
import time
import math
import pytest


sites = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']


def get_answer():
    return str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Safari()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', sites)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    input_answer = browser.find_element_by_css_selector('.textarea')
    input_answer.send_keys(get_answer())
    button = browser.find_element_by_class_name('submit-submission')
    button.click()
    answer_result = browser.find_element_by_class_name('smart-hints__hint').text
    assert answer_result == 'Correct!', "Wrong result"
