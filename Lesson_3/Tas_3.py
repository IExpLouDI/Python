# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def myfunc(a):
    sum = 0
    a.sort()
    for i in range(1, len(a)):
        sum = sum + a[i]
    return sum
a = []
for i in range(3):
    a.append(float(input(f"Введите {i + 1} число: ")))
sum = myfunc(a)
print(sum)