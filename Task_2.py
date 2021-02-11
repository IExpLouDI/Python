a = []
count = int(input("Сколько элементов хотите добавить в список? "))
for i in range(count):
     a.append(input("Введите число: "))
print(a)
for i in range(1, len(a), 2):
     a[i], a[i - 1] = a[i - 1], a[i]
print(f"Ваш список после перестановка местами будет выглядить так\n {a}")

