# 3.2 Регулярные выражения в Python
##############################
# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен),
# на слово "argh".
# Примечание:
# Обратите внимание на параметр count у функции sub.
import sys
import re


pattern = r'\b[aA]+\b'
for line in sys.stdin:
    line = line.rstrip()
    if line:
        print(re.sub(pattern, 'argh', line, count=1))
    else:
        break
