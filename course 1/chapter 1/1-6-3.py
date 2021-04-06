import time
# 1.6 Наследование классов
##############################
# Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, чтобы при добавлении
# элемента в список посредством метода append в лог отправлялось сообщение, состоящее из только что
# добавленного элемента.


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, var):
        super(LoggableList, self).append(var)
        self.log(var)
