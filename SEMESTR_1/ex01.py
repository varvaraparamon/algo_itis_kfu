"""
Для введенного n вывести «трифорс» (пример ниже), n - высота каждого треугольника. 
Не использовать строки и массивы символов.
"""

n = int(input())

for i in range(1, n + 1):
    for _ in range(n*2 - i + 1):
        print(" ", end="")
    for _ in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(1, n + 1):    
    for _ in range(n - i + 1):
        print(" ", end="")
    for _ in range(2 * i - 1):
        print("*", end="")

    for _ in range(2*(n-i)+1):
        print(" ", end="")
    for _ in range(2 * i - 1):
        print("*", end="")
    print()
