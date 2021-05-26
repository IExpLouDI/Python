# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.


class WareHouse:
    __printer = []
    __scaner = []
    __photocopier = []
    __direct_list = [{'Имя': 'Север', 'Принтер': 0, 'Сканер': 0, 'Ксерокс': 0},
                     {'Имя': 'Юг', 'Принтер': 0, 'Сканер': 0, 'Ксерокс': 0},
                     {'Имя': 'Запад', 'Принтер': 0, 'Сканер': 0, 'Ксерокс': 0},
                     {'Имя': 'Восток', 'Принтер': 0, 'Сканер': 0, 'Ксерокс': 0}]

    def printer_add(self, dictionary):
        self.__printer.append(dictionary)

    def obj_add(self, dictionary, us_ch):
        if us_ch == 1:
            self.__printer.append(dictionary)
        elif us_ch == 2:
            self.__scaner.append(dictionary)
        elif us_ch == 3:
            self.__photocopier.append(dictionary)

    def show_info(self):
        memory = ''
        for a in range(len(self.__direct_list)):
            shad_ar = [str(el) for el in self.__direct_list[a].values()]
            memory += f'\nОфис: "{shad_ar[0]}".\nПринтеров: {str(shad_ar[1])}' \
                      f'\nСканеров: {str(shad_ar[2])}\n' \
                      f'Ксероксов: {str(shad_ar[3])}\n'
        print(memory)

    def show_printer_list(self):
        memory = ''
        for a in range(len(self.__printer)):
            memory += f'{a + 1}: ' + '-'.join([str(el) for el in self.__printer[a].values()]) + '\n'
        return memory

    def show_scaner_list(self):
        memory = ''
        for a in range(len(self.__scaner)):
            memory += f'{a + 1}: ' + '-'.join([str(el) for el in self.__scaner[a].values()]) + '\n'
        return memory

    def show_photocopier_list(self):
        memory = ''
        for a in range(len(self.__photocopier)):
            memory += f'{a + 1}: ' + '-'.join([str(el) for el in self.__photocopier[a].values()]) + '\n'
        return memory

    def dir_object(self, my_list):
        ar_key = ('Принтер', 'Сканер', 'Ксерокс')
        if my_list[1] == 1:
            self.__direct_list[my_list[0] - 1][ar_key[my_list[1] - 1]] += my_list[3]
            self.__printer[my_list[2] - 1]['Quantity:'] -= my_list[3]
        elif my_list[1] == 2:
            self.__direct_list[my_list[0] - 1][ar_key[my_list[1] - 1]] += my_list[3]
            self.__scaner[my_list[2] - 1]['Quantity:'] -= my_list[3]
        elif my_list[1] == 3:
            self.__direct_list[my_list[0] - 1][ar_key[my_list[1] - 1]] += my_list[3]
            self.__photocopier[my_list[2] - 1]['Quantity:'] -= my_list[3]


class OfficeEquipment:
    def __init__(self, quantity):
        self.quantity = quantity


class Printer(OfficeEquipment):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.md = {'Name:': name, 'Quantity:': quantity, 'Value:': 'штук'}

    def printer_add(self):
        return self.md


class Scanner(OfficeEquipment):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.md = {'Name:': name, 'Quantity:': quantity, 'Value:': 'штук'}

    def scan_add(self):
        return self.md


class Photocopier(OfficeEquipment):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.md = {'Name:': name, 'Quantity:': quantity, 'Value:': 'штук'}

    def photocopier_add(self):
        return self.md


wh = WareHouse()
user_choise = 1
us_ch_an = 1

while user_choise != 0:
    try:
        user_choise = int(input('Выберите действие:\n1 - добавить предмет на склад;'
                                '\n2 - просмотреть список;\n3 - отправить в офис;\n0 - выйти из программы.\n'))
        if user_choise == 1:
            while us_ch_an != 0:
                us_ch_an = int(input('Выберите действие:\n1 - добавить принтер;'
                                     '\n2 - добавить сканер;\n3 - добавить ксерокс;\n'
                                     '0 - вернуться в основное меню.\n'))
                if us_ch_an == 1:
                    name = input('Название: ')
                    quantity = int(input('Количество: '))
                    p_q = Printer(name, quantity)
                    wh.obj_add(p_q.printer_add(), us_ch_an)

                elif us_ch_an == 2:
                    name = input('Название: ')
                    quantity = int(input('Количество: '))
                    p_s = Scanner(name, quantity)
                    wh.obj_add(p_s.scan_add(), us_ch_an)

                elif us_ch_an == 3:
                    name = input('Название: ')
                    quantity = int(input('Количество: '))
                    ph_q = Photocopier(name, quantity)
                    wh.obj_add(ph_q.photocopier_add(), us_ch_an)

        elif user_choise == 2:
            us_ch_an = int(input('Выберите действие:\n1 - вывести список принтеров;'
                                 '\n2 - вывести список сканеров;\n3 - вывести список ксероксов;\n'
                                 '4 - список отделов и оборудовния;\n'))
            if us_ch_an == 1:
                print(wh.show_printer_list())
            elif us_ch_an == 2:
                print(wh.show_scaner_list())
            elif us_ch_an == 3:
                print(wh.show_photocopier_list())
            elif us_ch_an == 4:
                wh.show_info()

        elif user_choise == 3:
            print(f"Оборудование в наличии:\nПринтеры:\n{wh.show_printer_list()}"
                  f"Сканеры:\n{wh.show_scaner_list()}Ксероксы:\n{wh.show_photocopier_list()}")
            us_ch_an = input('Введите код через знак "-":\n'
                             'Код офиса: 1 - Севере, 2 - Юг, 3 - Запад, 4 - Восток\n'
                             'Код оборудования: 1 - Принтер, 2 - Сканер, 3 - Ксерокс\n'
                             'Номер из списка:\n'
                             'Количество оборудования из наличия на складе:\n'
                             'Пример кода: 1-1-1-2\n')
            us_ch_an = [int(el) for el in us_ch_an.split('-')]
            wh.dir_object(us_ch_an)
            pass

    except Exception as err:
        print(err)
