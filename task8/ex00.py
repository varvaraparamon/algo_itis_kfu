"""
1. Написать функцию, которая получает целое число x и выдает
округленное вниз до ближайшего целого значение квадратного корня от х.
Сложность O(log x)
"""

from plot import *

def my_sqrt(x):
    l, r = 0, x
    while l <= r:
        mid = (l+r)//2
        if (x == mid**2):
            return mid
        elif (x < mid**2):
            r = mid - 1
        else:
            l = mid + 1
    return r



if __name__ == "__main__":
    #print(list(map(lambda x: my_sqrt(x), [1, 9, 16, 25, 26, 99]))) - примеры

    sizes = [10 ** i for i in range(1, 7)]
    time_func_mean = []
    time_func_min = []
    time_func_max = []

    for size in sizes:
        a = random.randint(size, 10 * size)

        mean_func, min_func, max_func= measure_time(my_sqrt, a)
        time_func_mean.append(mean_func)
        time_func_min.append(min_func)
        time_func_max.append(max_func)

    plt.figure(figsize=(12, 6))

    plt.plot(sizes, time_func_mean, label="my_sqrt", marker='o', color='blue')

    plt.fill_between(sizes, time_func_min, time_func_max, alpha=0.2, color='blue')

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Размер чисел")
    plt.ylabel("Время выполнения (секунды)")
    plt.title("Выполнение my_sqrt")
    plt.legend()
    plt.grid(True)
    plt.show()