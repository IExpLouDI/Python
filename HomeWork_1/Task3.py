#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."

us_num = int(input('Enter number from 1 to 9: '))
count = 1
s = 0

while count <= 3:
  s += int(count * str(us_num))
  count += 1

print(s)