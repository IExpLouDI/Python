# Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, date):
        self.date = date

    @staticmethod
    def valid_date(d, m, y):
        if d >= 32:
            return False
        if m > 12:
            return False
        if y != 2021:
            return False
        return True

    @classmethod
    def num_date(cls, date):
        try:

            d, m, y = [int(el) for el in date.split('-')]

            if cls.valid_date(d, m, y) is False:
                return cls(f"Error").date

            return cls.valid_date(d, m, y)

        except Exception as err:
            return cls(f"Error!\n{err}").date


one = Data.num_date(input('Введите дату в формате дд-мм-гггг (10-10-2021):\n'))
print(one)
