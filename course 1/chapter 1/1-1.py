# 1.1 Введение
##############################
# Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.
# Вашей программе на вход подается последовательность строк.
# Первая строка содержит число n (1 ≤ n ≤ 100).
# В следующих n строках содержится по одному целому числу.
# Выведите одно число – сумму данных n чисел.

number_count = int(input())
numbers_list = []
numbers_sum = 0

for i in range(number_count):
    new_n = int(input())
    numbers_list.append(new_n)


for i in numbers_list:
    numbers_sum += i

print(numbers_sum)
