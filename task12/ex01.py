"""
Даны два массива x[1] . . . x[k] и y[1] . . . y[l] и число q. Найти сумму вида x[i]
+ y[j], наиболее близкую к числу q. (Число действий порядка k+l, дополнительная
память — фиксированное число целых переменных, сами массивы менять не
разрешается.)
"""

import time
import numpy as np

def nearest_sum(x, y, q):
    i, j = 0, len(y) - 1
    min_diff = float('inf')
    closest_sum = 0
    best_i, best_j = -1, -1

    while i < len(x) and j >= 0:
        s = x[i] + y[j]
        diff = abs(q - s)

        if diff < min_diff:
            min_diff = diff
            closest_sum = s
            best_i, best_j = i, j
        if s < q:
            i += 1
        else:
            j -= 1
    return x[best_i], y[best_j], closest_sum 

def measure_time(func, *args, repeats=10):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times)


x = [1, 3, 4, 5, 6, 6, 6, 7, 8, 10]
y = [4, 6, 7, 8, 8, 9, 12, 13]

q = 13
print(nearest_sum(x, y, q))
print(measure_time(nearest_sum, x, y, q))

