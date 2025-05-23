"""
3. Удаление всех дубликатов из списка
- С использованием множества: Преобразовать список в множество и обратно в список. Сложность: O(n)
- Без множества: Пройтись по списку и добавлять в новый список только уникальные элементы. Сложность: O(n^2)
"""
import random
import time
import numpy as np
import matplotlib.pyplot as plt

def drop_dubl1(a):
    a_set = set(a)

    return list(a_set)


def drop_dubl2(a):
    unique = []
    for i in range(len(a)):
        flag = True
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                flag = False     
        if flag:
            unique.append(a[i])
    return unique



def measure_time(func, *args, repeats=10):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times), np.min(times), np.max(times)

if __name__ == "__main__":
    sizes = [50, 100, 150, 200, 250]
    time_mean = []
    time_min = []
    time_max = []

    time_2mean = []
    time_2min = []
    time_2max = []

    for size in sizes:
        a = [random.randint(1, 10 * size) for i in range(size)]
        mean_1, min_1, max_1 = measure_time(drop_dubl1, a)
        time_mean.append(mean_1)
        time_min.append(min_1)
        time_max.append(max_1)

        mean_2, min_2, max_2 = measure_time(drop_dubl2, a)
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