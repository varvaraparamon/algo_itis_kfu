import random
import time
import numpy as np
import matplotlib.pyplot as plt


def gcd(a, b):
    pass


def gcd2(a, b):
    pass


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
    time_gcd_mean = []
    time_gcd_min = []
    time_gcd_max = []

    time_gcd2_mean = []
    time_gcd2_min = []
    time_gcd2_max = []

    for size in sizes:
        a = random.randint(size, 10 * size)
        b = 15

        mean_gcd, min_gcd, max_gcd = measure_time(gcd, a, b)
        time_gcd_mean.append(mean_gcd)
        time_gcd_min.append(min_gcd)
        time_gcd_max.append(max_gcd)

        mean_gcd2, min_gcd2, max_gcd2 = measure_time(gcd2, a, b)
        time_gcd2_mean.append(mean_gcd2)
        time_gcd2_min.append(min_gcd2)
        time_gcd2_max.append(max_gcd2)

        print(f"Размер: {size}")
        print(f"GCD (деление): среднее={mean_gcd:.10f}, мин={min_gcd:.10f}, макс={max_gcd:.10f}")
        print(f"GCD2 (вычитание): среднее={mean_gcd2:.10f}, мин={min_gcd2:.10f}, макс={max_gcd2:.10f}")
        print("------")

    plt.figure(figsize=(12, 6))

    '''
        Основная линия (plt.plot()) показывает среднее время выполнения
    '''
    plt.plot(sizes, time_gcd_mean, label="GCD (деление с остатком)", marker='o', color='blue')

    '''
        sizes: Список значений по оси X, которые соответствуют размерам входных чисел. 
        Это точки, между которыми будет заливаться область
        
        time_gcd_min, time_gcd_max: Списки минимального и максимального времени выполнения 
        алгоритма GCD для каждого размера чисел. Они задают границы области заливки по оси Y.
        
        alpha: Уровень прозрачности заливки (от 0 до 1). 
        Значение 0.2 делает область полупрозрачной, чтобы не перекрывать основные линии графика
    '''
    plt.fill_between(sizes, time_gcd_min, time_gcd_max, alpha=0.2, color='blue')

    plt.plot(sizes, time_gcd2_mean, label="GCD2 (вычитание)", marker='o', color='orange')
    plt.fill_between(sizes, time_gcd2_min, time_gcd2_max, alpha=0.2, color='orange')

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Размер чисел")
    plt.ylabel("Время выполнения (секунды)")
    plt.title("Сравнение GCD и GCD2")
    plt.legend()
    plt.grid(True)
    plt.show()