# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки!')


class Pen(Stationary):

    def draw(self):
        print(f'Запуск отрисовки {self.title}.')


class Pencil(Stationary):
    def draw(self):
        print(f'Запуск отрисовки {self.title}.')


class Handle(Stationary):
    def draw(self):
        print(f'Запуск отрисовки {self.title}.')


a = Pen('ручкой')
a.draw()
b = Pencil('карандашом')
b.draw()
f = Handle('маркером')
f.draw()
