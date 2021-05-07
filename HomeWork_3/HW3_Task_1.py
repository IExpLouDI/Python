# Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль

def my_func(a, b):
  try:
    return a / b
  except ZeroDivisionError as zer:
    return f"{zer}"

var_1 = int(input("Enter first number: "))
var_2 = int(input("Enter first number: "))

var_3 = my_func(var_1, var_2)

print(var_3)
