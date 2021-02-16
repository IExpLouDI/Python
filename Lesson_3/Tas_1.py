# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.
def myfunc(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        print("Error")
        return
    c = a / b
    return c
a = int(input("Введите делимое:\n"))
b = int(input("Введите делитель:\n"))
c = myfunc(a, b)
print(c)