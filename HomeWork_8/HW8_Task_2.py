# Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MuTrubble(Exception):
    def __init__(self, text):
        self.text = text


a = input('Делимое: ')
b = input('Делитель: ')

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise MuTrubble('Are you seriosly?? 0!!')
    print(f'Частное = {a / b:.2f}')
except (ValueError, MuTrubble) as err:
    print(err)
