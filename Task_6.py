spisok = []
korteg = ()
dictionary = {}
stats = {}
number = int(input("Сколько позиций хотите внести в список? "))
for i in range(number):
   dictionary = dict(Name = input("Введите название: "), Price = float(input("Введите стоимость: ")),
    Count = int(input("Введите количество: ")), Dimension = input("Введите размерность: "))
   korteg = (i +1 , dictionary)
   spisok.append(korteg)
print(spisok)
s = input("Введите желаемый параметр: Name, Price, Count, Dimension.\n").title()
cut = []
for i in spisok:
    cut.append(i[1].get(s))
stats = {s: cut}
print(stats)
