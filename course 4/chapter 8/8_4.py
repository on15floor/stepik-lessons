"""8.4. Основы работы с множествами."""
"""8.4.6.Дополните приведенный код так, чтобы он вывел сумму минимального и максимального элементов множества numbers.
"""
numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
print(min(numbers) + max(numbers))

"""8.4.7.Дополните приведенный код, чтобы он вывел среднее арифметическое элементов множества numbers.
"""
numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
average = sum(numbers) / len(numbers)
print(average)

"""8.4.10.Дополните приведенный код, чтобы он вывел сумму квадратов элементов множества numbers.
"""
numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
res = 0
for num in numbers:
    res += num * num
print(res)

"""8.4.11.Дополните приведенный код, чтобы он вывел элементы множества fruits, каждый на отдельной строке, 
отсортированные по убыванию (в обратном лексикографическом порядке)."""
fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
fruits_sorted = sorted(fruits, reverse=True)
print(*fruits_sorted, sep='\n')

"""8.4.12.На вход программе подается строка текста. Напишите программу, которая определяет количество различных 
символов в строке."""
print(len(set(input())))

"""8.4.13.На вход программе подается строка, состоящая из цифр. Необходимо определить, верно ли, что в ее записи 
ни одна из цифр не повторяется?"""
s = input()
print('YES' if len(s) == len(set(s)) else 'NO')

"""8.4.14.На вход программе подаются две строки, состоящие из цифр. Необходимо определить, верно ли, что в записи 
этих двух строк используются все десять цифр?"""
s = input() + input()
print('YES' if len(set(s)) == 10 else 'NO')

"""8.4.15.На вход программе подаются две строки, состоящие из цифр. Необходимо определить, верно ли, что для 
записи этих строк были использованы одинаковые наборы цифр?"""
s1, s2 = input(), input()
print('YES' if set(s1) == set(s2) else 'NO')

"""8.4.16.На вход программе подается строка, состоящая из трех слов. Верно ли, что для записи всех трех слов был 
использован один и тот же набор букв?"""
s = input().split()
print('YES' if set(s[0]) == set(s[1]) == set(s[2]) else 'NO')