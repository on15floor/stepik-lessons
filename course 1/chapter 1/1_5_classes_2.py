# 1.5 Введение в классы
##############################
# Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел из
# этой последовательности, затем сумму второй пятерки, и т. д.
# Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части.
# Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.
# Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок
# последовательных элементов по мере их накопления.
# Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно
# необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.

class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *args):
        for a in args:
            self.buffer.append(a)
        while len(self.buffer) >= 5:
            buffer_sum = 0
            for i in range(5):
                buffer_sum += self.buffer[i]
            self.buffer = self.buffer[5:]
            print(buffer_sum)

    def get_current_part(self):
        return self.buffer
