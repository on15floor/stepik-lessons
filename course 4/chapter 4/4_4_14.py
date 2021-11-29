"""4. Матрицы. Часть 1.
Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями:
верхнюю, нижнюю, левую и правую.
Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти;
левой четверти.
"""
n = int(input())
matrix = []
count1 = 0  # Верхняя четверть
count2 = 0  # Правая четверть
count3 = 0  # Нижняя четверть
count4 = 0  # Левая четверть

for _ in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
count = matrix[0][0]

for i in range(n):
    for j in range(n):
        if i < j and i < n-1-j:
            count1 += matrix[i][j]
        if j > i > n-1-j:
            count2 += matrix[i][j]
        if i > j and i > n-1-j:
            count3 += matrix[i][j]
        if j < i < n-1-j:
            count4 += matrix[i][j]

print('Верхняя четверть:', count1)
print('Правая четверть:', count2)
print('Нижняя четверть:', count3)
print('Левая четверть:', count4)
