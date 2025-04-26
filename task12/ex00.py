"""
Дан числовой массив размерности n, упорядоченный по неубыванию. Для
некоторого числа а найти нижний и верхний индексы элементов равных этому
числу. При отсутствии в массиве такого числа возвращается значение 0.
(Сложность O(log n))
"""

import time
import numpy as np

def lower_find(a, x):
    lower_bound = 0
    l, r = 0, len(a) - 1
    while l <= r:
        mid = (l+r)//2
        if a[mid] > x:
            r = mid - 1
        elif a[mid] < x:
            l = mid + 1
        else:
            lower_bound = mid
            r = mid - 1

    return lower_bound

def upper_find(a, x):
    upper_bound = 0
    l, r = 0, len(a) - 1
    while l <= r:
        mid = (l+r)//2
        if a[mid] > x:
            r = mid - 1
        elif a[mid] < x:
            l = mid + 1
        else:
            upper_bound = mid
            l = mid + 1

    return upper_bound



def measure_time(func, *args, repeats=10):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times)


x = int(input())
a = list(map(int, input().strip().split()))
# x = 3
# a = [1, 2, 3, 3, 3, 4, 4, 5, 66]
print(lower_find(a, x), upper_find(a, x))
print(measure_time(lower_find, a, x), measure_time(upper_find, a, x))

