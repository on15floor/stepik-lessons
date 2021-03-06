# 2.3 Итераторы и генераторы
##############################
# Одним из самых часто используемых классов в Python является класс filter. Он принимает в конструкторе два
# аргумента a и f – последовательность и функцию, и позволяет проитерироваться только по таким элементам x из
# последовательности a, что f(x) равно True. Будем говорить, что в этом случае функция f допускает элемент x,
# а элемент x является допущенным....


class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos > 0

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterator = iter(iterable)
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            elem = next(self.iterator)
            pos, neg = 0, 0
            for func in self.funcs:
                if func(elem):
                    pos += 1
                else:
                    neg += 1

            if self.judge(pos, neg):
                return elem


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]
