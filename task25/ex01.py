"""
Создайте программу, которая эффективно вычисляет число оконечных
нулей в двоичном представлении целого положительного числа.
"""
import timeit

def last_null(n):
    if n == 0:
        return "error"
    if (n&1) == 1:
        return 0
    else:
        return 1 + last_null(n//2)

print(last_null(40))
print(timeit.timeit(lambda : last_null(40), number=1000)/1000)