# 3.2 Регулярные выражения в Python
##############################
# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
import sys
import re

pattern = r'((cat).*){2,}'
for line in sys.stdin:
    line = line.rstrip()
    if line:
        if re.search(pattern, line):
            print(line)
    else:
        break
