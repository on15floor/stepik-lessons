"""3.2 Тестирование web-приложений и тестовые фреймворки
Попробуйте оформить тесты из первого модуля в стиле unittest.
Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание."""

from selenium import webdriver
import unittest
import time


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Safari()
        link = 'http://suninjuly.github.io/registration1.html'
        browser.get(link)
        input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys('First')
        input2 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys('Second')
        input3 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys('Email')
        input4 = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[1]/input')
        input4.send_keys('Phone')
        input5 = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[2]/input')
        input5.send_keys('Address')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        res = browser.find_element_by_tag_name('h1').text
        browser.quit()
        print(res)
        self.assertIn('Congratulations', res, "Something go wrong")

    def test_abs2(self):
        browser = webdriver.Safari()
        link = 'http://suninjuly.github.io/registration2.html'
        browser.get(link)
        input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys('First')
        input2 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys('Second')
        input3 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys('Email')
        input4 = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[1]/input')
        input4.send_keys('Phone')
        input5 = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[2]/input')
        input5.send_keys('Address')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        res = browser.find_element_by_tag_name('h1').text
        browser.quit()
        print(res)
        self.assertIn('Congratulations', res, "Something go wrong")


if __name__ == "__main__":
    unittest.main()
