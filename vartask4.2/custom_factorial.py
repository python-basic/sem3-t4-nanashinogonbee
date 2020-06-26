import re


def factorial(n):
    if '.' in str(n):
        raise ValueError("Факториала от дробного числа не существует!")
    elif not re.sub('\.|\-', '', str(n)).isdigit():
        raise TypeError("Аргумент не является числом!")
    elif float(n) < 0:
        raise ValueError("Факториала от отрицательного числа не существует!")
    else:
        n = int(n)
        return 1 if not n else n * factorial(n - 1)


print(f'n! = {factorial(input("Введите число n: "))}')
