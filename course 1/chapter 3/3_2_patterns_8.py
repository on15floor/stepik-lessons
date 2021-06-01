# 3.2 Регулярные выражения в Python
##############################
# Вам дана последовательность строк.
# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.
import sys
import re


pattern = r'\b(\w)(\w)(\w*)\b'
for line in sys.stdin:
    line = line.rstrip()
    if line:
        print(re.sub(pattern, r'\2\1\3', line))
    else:
        break
