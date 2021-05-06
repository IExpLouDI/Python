# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой

def my_func(v_1, v_2, v_3, v_4, v_5, v_6):
    print(' '.join(['\n', 'Name:', v_1, 'Second name:', v_2, 'Birthday date:',
                    v_3, 'City:', v_4, 'Email:', v_5, 'Telefon number:', v_6]))


name = input('Name: ') + '\n'
sec_name = input('Second name: ') + '\n'
birh_date = input('Birth day date: ') + '\n'
city = input('City: ') + '\n'
mail = input('Email: ') + '\n'
tel_num = input('Telefon number: ') + '\n'

my_func(name, sec_name, birh_date, city, mail, tel_num)
