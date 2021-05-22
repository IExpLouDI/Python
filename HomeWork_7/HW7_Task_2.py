# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size):
        self.size = size

    @abstractmethod
    def consumption(self):
        pass


class Blazer(Clothes):

    def __init__(self, size):
        super().__init__(size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if 30 <= size <= 90:
            self.__size = size
        elif size > 90:
            self.__size = 90
        else:
            self.__size = 30

    def consumption(self):
        return self.__size / 6.5 + 0.5


class Coat(Clothes):

    def __init__(self, size):
        super().__init__(size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if 150 <= size <= 200:
            self.__size = size
        elif size > 200:
            self.__size = 200
        else:
            self.__size = 150

    def consumption(self):
        return self.__size * 2 / 100 + 0.3


a = Blazer(30)
b = Coat(189)
print(f"Расход ткани на пиджак:\n{a.consumption():.2f}\nРасход ткани на пальто:\n{b.consumption():.2f}\n"
      f"Суммарный расход ткани будет = {a.consumption() + b.consumption():.2f}")
