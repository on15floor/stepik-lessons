# 3.2 Регулярные выражения в Python
##############################
# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
import sys
import re

pattern = r'z[a-z]{3}z'
for line in sys.stdin:
    line = line.rstrip()
    if line:
        if re.search(pattern, line):
            print(line)
    else:
        break
