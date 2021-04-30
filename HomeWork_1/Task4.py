# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции."

us_num = int(input("Enter random number: "))
max_num = 0
count = len(str(us_num))

while count > 0:

  if us_num % 10 > max_num:
    max_num = us_num % 10
  us_num = us_num // 10
  count -= 1

print(max_num)