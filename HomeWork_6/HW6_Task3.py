# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': income[0], 'bonus': income[1]}


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(f'Position: {self.position}.\nName: {self.name}.\nSecond name: {self.surname}')

    def get_total_income(self):
        print(f"Total income: {sum(self._income.values())}")


a = Position('Fernand', 'Markuolis', 'Garden manager', [150, 12])
a.get_full_name()
a.get_total_income()
b = Position('Grisha', 'Lebedev', 'Student', [20, 1])
b.get_full_name()
b.get_total_income()
