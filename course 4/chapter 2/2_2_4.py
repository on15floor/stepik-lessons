"""2. Повторяем основные конструкции языка Python. Часть 2.
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым,
а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.
"""
s = input().split()
s.insert(0, s.pop(len(s)-1))
print(' '.join(str(x) for x in s))
