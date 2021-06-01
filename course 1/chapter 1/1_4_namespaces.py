# 1.4 Пространства имён и области видимости
##############################
# Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку
# создания пространств имен и добавление в них переменных.

pt = 'parent'
vs = 'vars'
namespaces = {'global': {pt: '', vs: []}}


def create(ns, parent):
    if ns not in namespaces:
        namespaces[ns] = {pt: parent, vs: []}


def add(ns, var):
    if ns in namespaces:
        namespaces[ns][vs].append(var)


def get(ns, var):
    if ns == 'global':
        print('None' if var not in namespaces[ns][vs] else ns)
    elif var in namespaces[ns][vs]:
        print(ns)
    else:
        get(namespaces[ns][pt], var)


n = int(input())
for i in range(n):
    cmd, p1, p2 = input().split()
    if cmd == 'create':
        create(p1, p2)
    elif cmd == 'add':
        add(p1, p2)
    elif cmd == 'get':
        get(p1, p2)
