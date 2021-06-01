# 1.6 Наследование классов
##############################
# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

# словарь наследник : предки
child_parents_dict = {}


def find_cls(a, b):
    if a == b:
        return True
    elif a in child_parents_dict[b]:
        return True
    else:
        for c in child_parents_dict[b]:
            if find_cls(a, c):
                return True
        return False


for i in range(int(input())):
    inp = str(input()).split()
    child_parents_dict.update({inp[0]: set(inp[2:])})


for i in range(int(input())):
    inp = (str(input()).split())
    cls1, cls2 = inp[0], inp[1]
    if find_cls(cls1, cls2):
        print("Yes")
    else:
        print("No")
