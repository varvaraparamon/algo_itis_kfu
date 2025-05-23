"""
1. Проверка на наличие дубликатов в списке
- С использованием множества: Сложность: O(n)
- Без множества: Пройтись по всем элементам списка и проверять каждый элемент с остальными (двойной цикл). Сложность: O(n^2)
"""

import random
import time
import numpy as np
import matplotlib.pyplot as plt


def find_duplicates1(a):
    a_set = set(a)
    if len(a_set) != len(a):
        return True
    return False


def find_duplicates2(a):

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return True        
    return False


def measure_time(func, *args, repeats=10):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times), np.min(times), np.max(times)

if __name__ == "__main__":
    sizes = [10 ** i for i in range(1, 7)]
    time_mean = []
    time_min = []
    time_max = []

    time_2mean = []
    time_2min = []
    time_2max = []

    for size in sizes:
        a = [random.randint(1, 10 * size) for i in range(size)]
        mean_1, min_1, max_1 = measure_time(find_duplicates1, a)
        time_mean.append(mean_1)
        time_min.append(min_1)
        time_max.append(max_1)

        mean_2, min_2, max_2 = measure_time(find_duplicates2, a)
        time_2mean.append(mean_2)
        time_2min.append(min_2)
        time_2max.append(max_2)


    plt.figure(figsize=(12, 6))

    plt.plot(sizes, time_mean, label="1", marker='o', color='blue')

    plt.fill_between(sizes, time_min, time_max, alpha=0.2, color='blue')

    plt.plot(sizes, time_2mean, label="2", marker='o', color='orange')
    plt.fill_between(sizes, time_2min, time_2max, alpha=0.2, color='orange')

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Размер чисел")
    plt.ylabel("Время выполнения (секунды)")
    plt.title("Сравнение")
    plt.legend()
    plt.grid(True)
    plt.show()