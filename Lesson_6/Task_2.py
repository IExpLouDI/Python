# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    _density = 25
    _thikness = 5
    def road_mass(self, width, length):
        self._width = width
        self._length = length
        _mass = self._width * self._length * Road._density * Road._thikness
        return _mass

x = Road()
y = Road()
mass = x.road_mass(2, 1)
print(mass, mass2)
