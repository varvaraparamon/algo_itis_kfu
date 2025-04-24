"""
Найти ряд Маклорена для функции exp(x) и вычислить ее с точностью 1e-9.
"""

from math import exp

x = float(input())
el = 1
expx = 1

i = 1
while el >= 10**-9:
    el = el*x/i
    expx += el
    i += 1

print(f"{expx:.9f} - разложение в ряд маклорена")
print(f"{exp(x):.9f} - оригинальный exp")