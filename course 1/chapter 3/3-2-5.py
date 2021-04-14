# 3.2 Регулярные выражения в Python
##############################
# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
import sys
import re

pattern = r'\b(.+)\1\b'
for line in sys.stdin:
    line = line.rstrip()
    if line:
        if re.search(pattern, line):
            print(line)
    else:
        break
