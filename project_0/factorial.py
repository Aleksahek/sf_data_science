#!/bin/python3
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Введите число: "))
print("Факториал числа", number, "равен", factorial(number))
