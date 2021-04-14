# 3.2 Регулярные выражения в Python
##############################
# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.
import sys
import re

pattern = r'human'
for line in sys.stdin:
    line = line.rstrip()
    if line:
        print(re.sub(pattern, 'computer', line))
    else:
        break
