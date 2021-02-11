import random
a = []
b = int(input("Введите количество элементов в списке: "))
for i in range(b):
    a.append(random.randint(0, 9))
a.sort(reverse=True)
print(f"Реультат генерации: \n {a}")
count = int(input("Сколько элементов добавить в список? "))
for i in range(count):
    a.append(int(input("Число от 0 до 9: ")))
    for j in range(len(a)):
        if a[len(a) - 1] > a[j]:
            a[len(a) - 1], a[j] = a[j], a[len(a) - 1]
            continue
print(f"Ваш список после добавления будет:\n{a}")

