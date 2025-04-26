"""
Дана последовательность различных чисел, в которой все числа до
определенного индекса j отсортированы по убыванию, а после j по возрастанию.
Найдите этот индекс j. (Сложность O(log n).)
"""
import time
import numpy as np

def perelom(a):
    l, r = 0, len(a) - 1
    j = 0
    while (l < r):
        mid = (l+r)//2
        if (a[mid] > a[mid+1]):
            l = mid + 1
        else:
            r = mid

    return (l)





def measure_time(func, *args, repeats=10):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times)

a = [9, 7, 5, 3, 4, 6, 8]
print(perelom(a))
print(measure_time(perelom, a))