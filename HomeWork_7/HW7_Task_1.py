# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix.
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = '\n'
        for i in range(len(self.matrix)):
            s += ' '.join([str(el) for el in self.matrix[i]]) + '\n'
        return s

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(self.matrix)
        pass


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
matrix_3 = Matrix([[19, 20, 21], [22, 23, 24], [25, 26, 27]])

print(f'Матрица 1:{matrix_1}Матрица 2:{matrix_2}Матрица 3:{matrix_3}'
      f'Сумма матриц Матрица 1 + Матрица 2 + Матрица 3:{matrix_1 + matrix_2 + matrix_3}')
