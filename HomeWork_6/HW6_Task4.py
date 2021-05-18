# Реализуйте базовый класс Car
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
from random import randint


class Car:
    speed = 10
    color = 'red'
    name = 'Mazda'
    is_police = bool

    def go(self):
        print('Leeeeets gooooo!')

    def stop(self):
        print('STOP!')

    def turn(self):
        chance = randint(0, 1)
        turn_side = ['right', 'left']
        print(f'Car turn the {turn_side[chance]}!')

    def show_speed(self):
        print(f'Your speed is {self.speed} km/h.')


class TownCar(Car):

    def __init__(self, speed):
        self.speed = speed

    def show_speed(self):
        if self.speed > 60:
            print(f'Plz more slowly dude! OMG {self.speed}')
        else:
            print(f'It`s nice speed man. I can relax for {self.speed} km/h!')


class SportCar(Car):
    pass


class WorkCar(Car):

    def __init__(self, speed):
        self.speed = speed

    def show_speed(self):
        if int(self.speed) > 40:
            print(f'Plz more slowly dude! OMG {self.speed} km/h')
        else:
            print(f'It`s nice speed man. I can relax for {self.speed} km/h!')


class PoliceCar(Car):
    pass


a = TownCar(60)
a.go()
a.show_speed()
a.turn()
a.stop()

print()

b = WorkCar(90)
b.go()
b.show_speed()
b.turn()
b.stop()