"""8.2. Операции над множествами, диаграммы Эйлера-Венна.
На летних каникулах Тимур и ученики онлайн-школы BEEGEEK решили отдохнуть. В результате n учеников школы
поехали отдыхать на море, m учеников съездили в деревню, а k учеников сходили в горы. Оказалось, что и в деревне,
и на море были x учеников, а в деревне и в горах — y учеников. Побывать и в горах, и на море не удалось никому.
Напишите программу для определения количества учеников в школе, если никто не смог посетить все три места сразу, а
z учеников писали ДВИ по математике для поступления в МГУ, и никуда не ездили.
"""
n, m, k, x, y, z = [int(input()) for _ in range(6)]
print(z + m + k - y + n - x)
