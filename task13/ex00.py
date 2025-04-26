"""
В массиве a[1] . . . a[n] встречаются по одному разу все целые числа от 0 до n,
кроме одного. Найти пропущенное число за время порядка n и с конечной
дополнительной памятью.
"""
import time
import numpy as np

def find_num(a):
    n = len(a) + 1
    sum = 0

    for x in a:
        sum += x
    return(n*(n+1)/2 - sum)

def measure_time(func, *args, repeats=10):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times)

a = [1, 2, 3, 5, 6, 7]
print(find_num(a))
print(measure_time(find_num, a))

