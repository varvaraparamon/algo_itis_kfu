"""
Найти ряд Маклорена для функции sin(x) и вычислить ее с точностью 1e-9.
"""
from math import sin

x = float(input())
el = x
sinx = x

i = 3
while el >= 10**-9:
    el = el*(-1)*x*x/(i*(i-1))
    sinx += el
    i += 2

print(f"{sinx:.9f} - разложение в ряд маклорена")
print(f"{sin(x):.9f} - оригинальный синус")