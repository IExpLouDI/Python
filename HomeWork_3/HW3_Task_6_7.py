# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
# и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text

def int_func(string):
    memory = ' '.join(string).lower().split()

    for el in memory:
        if 97 <= ord(el) <= 122:
            continue
        elif el.isdigit() is True:
            continue
        else:
            return int_func(input('Введите слово или предложение из маленьких латинских букв: '))

    return string.title()


user_word = input("Введите слово или предложение из маленьких латинских букв: ")

print(int_func(user_word))
