"""
Для введенного n приблизительно нарисовать символами круг радиуcа n. Не использовать строки и массивы символов. Например, для n = 10:
"""
from math import *

radius = int(input())

for y in range(radius, -radius - 1, -1):
    x = -radius
    while x <= radius:
        if (y * y) + (x * x) < radius * radius:
            print("0", end='')
        else:
            print("*", end="")
        x += 0.5
    print()
    





