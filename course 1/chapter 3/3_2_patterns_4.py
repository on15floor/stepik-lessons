# 3.2 Регулярные выражения в Python
##############################
# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\".
import sys
import re

pattern = r'.*\\.*'
for line in sys.stdin:
    line = line.rstrip()
    if line:
        if re.search(pattern, line):
            print(line)
    else:
        break
