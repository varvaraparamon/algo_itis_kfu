"""
2. Есть кафельный пол размера N x M плиток. Все плитки квадратные.
Между ними небольшое расстояние. Пол порезали пилой-болгаркой по диагонали
от одного угла к противоположному по прямой. Вопрос: сколько плиток было
испорчено? Считать, что если линия разреза только касается плитки, то она не
портит ее. Сложность O(log max(N, M).
"""

from plot import *

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def count_damaged(n, m):
    return n+m - gcd(n, m)

if __name__ == "__main__":
    #print(list(map(lambda x: count_damaged(x[0], x[1]), [(1, 1), (2, 2), (3, 4)]))) - примеры
    sizes = [10 ** i for i in range(1, 7)]
    time_func_mean = []
    time_func_min = []
    time_func_max = []

    for size in sizes:
        b = 15
        a = random.randint(size, 10 * size)

        mean_func, min_func, max_func= measure_time(count_damaged, a, b)
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