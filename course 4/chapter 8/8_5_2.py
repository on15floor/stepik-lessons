"""8.2. Методы множеств. Часть 1.
Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.
На вход программе в первой строке подается число n – общее количество слов. Далее идут n строк с словами.
Программа должна вывести одно число – общее количество уникальных символов во всех словах без учета регистра.
"""
n = int(input())
words = ''
for i in range(0, n):
    words += input().lower()

print(len(set(words)))