"""2. Повторяем основные конструкции языка Python. Часть 1.
Дано пятизначное или шестизначное натуральное число. Напишите программу, которая изменит порядок
его последних пяти цифр на обратный.
"""


def revers(s: str) -> str:
    return s[::-1]


i_str = input()
i_int = int(i_str)        # Уберем нули, если есть
i_str = str(i_int)        # Вернем назад int
i_a = i_str[:-5]          # Возьмем все символы, кроме последних пяти
i_b = revers(i_str[-5:])  # Последние пять перевернем
print(int(i_a + i_b))
