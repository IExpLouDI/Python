# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение, вычитание, умножение, деление
# Данные методы должны применяться только к клеткам и выполнять
# увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell < other.cell:
            return 'Error'
        else:
            return Cell(self.cell - other.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        if self.cell < other.cell:
            return 'Error'
        else:
            return Cell(self.cell // other.cell)

    def __str__(self):
        return str(self.cell)

    def make_order(self, item):
        img_cell = '*'
        memory = ''
        count = self.cell
        while count > 0:

            if item > count:
                memory += img_cell * count + '\n'
                count -= item
            else:
                memory += img_cell * item + '\n'
                count -= item

        return memory


a = Cell(24)
b = Cell(13)
c = Cell(8)
print(a + b + c)
print(a - b - c)
print(a / (b / c))
print(a * b * c)
print(a.make_order(7))
print(b.make_order(3))
print(c.make_order(7))
