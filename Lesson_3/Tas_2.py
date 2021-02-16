# 2. Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def myfunc(name, sname, data, city, mail, telef):
    posit = name + " " + sname + " "  + data + " "  + city + " "  + mail + " "  + telef
    return posit
name = input("Имя: ")
sname = input("Фамилия: ")
data = input("Дата рождения: ")
city = input("Город: ")
mail = input("Электронная почта: ")
telef = input("Телефон для связи: ")
spisok = myfunc(name, sname, data, city, mail, telef)
print(spisok)