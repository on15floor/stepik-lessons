"""4. Вложенные списки. Вложенные списки. Часть 2.
На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает
последовательности одинаковых символов заданной строки в подсписки.
"""

input_str = input()
input_lst = input_str.split()
res_lst = []
tmp_lst = []
c = 0
for i in input_lst:
    c += 1
    if not tmp_lst:
        tmp_lst.append(i)
        continue
    if i in tmp_lst:
        tmp_lst.append(i)
    else:
        res_lst.append(tmp_lst)
        tmp_lst = [i]
    if c == len(input_lst):
        res_lst.append(tmp_lst)

print(res_lst)
