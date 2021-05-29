# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
from random import randint


class MyComplex:
    def __init__(self, imn, rel):
        self.my_complex = [imn, rel]

    def __str__(self):
        return f'{self.my_complex[0]} + {self.my_complex[1]}i'

    def __add__(self, other):
        return MyComplex(self.my_complex[0] + other.my_complex[0], self.my_complex[1] + other.my_complex[1])

    def __mul__(self, other):
        return MyComplex(self.my_complex[0] * other.my_complex[0] - self.my_complex[1] * other.my_complex[1],
                         self.my_complex[0] * other.my_complex[1] + self.my_complex[1] * other.my_complex[0])


a = MyComplex(randint(-5, 100), randint(-5, 100))
b = MyComplex(randint(-5, 100), randint(-5, 100))
print(f"Первое число: {a}")
print(f"Второе число: {b}")
print(f"Сумма комплексных чисел:\n{a + b}")
print(f"Произведение комплексных чисел:\n{a * b}")
