# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).
class Worker:
    _income = {"Генерал": [1400, 500], "Майор": [1200, 300], "Лейтенант": [1000, 200], "Дух": [500, 20]}
    table = [["Сергей", "Пупкин", "Генерал", _income["Генерал"]],
             ["Поликарп", "Земляничкин", "Майор", _income["Майор"]],
             ["Зигмунд", "Иванов", "Лейтенант", _income["Лейтенант"]],
             ["Дантес", "Пушкин", "Дух", _income["Дух"]]]

class Position(Worker):
    __name = ""
    __total = 0
    def get_full_name(self, value):
        self.position = value
        for i in range(len(Worker.table)):
            if self.position == Worker.table[i][2]:
                Position.__name += ' '.join(Worker.table[i][:2])
        return Position.__name
    def get_total_income(self, value):
        self.position = value
        for i in range(len(Worker.table)):
            if self.position == Worker.table[i][2]:
                for j in range(len(Worker.table[i][3])):
                    Position.__total += Worker.table[i][3][j]
        return Position.__total


item1 = Position()
position = input("Выберите должность: Генерал, Майор, Лейтенант, Дух.\n")
name = item1.get_full_name(position)
income = item1.get_total_income(position)
print(f"Сотрудник: {name}. Должность: {position}. Доход: {income} руб/месяц")

