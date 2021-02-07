usernum = int(input("Ваше число = "))
max = 0
while usernum > 0:
    if (usernum % 10) > max:
        max = usernum % 10
    usernum = usernum // 10

print(f"Самая большая цифра это {max}")

