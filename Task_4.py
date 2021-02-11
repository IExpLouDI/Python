a = input("Введите всё что вам угодно: ").split()
for i in range(len(a)):
    print(f"{i+1}-ая строка это {a[i][:10]}")