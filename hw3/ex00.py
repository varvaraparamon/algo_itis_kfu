from plot import *

def counter(b, p, a):
    res = 0
    for c in range(1, p):
        if (b*c)%p == a:
            res += 1
            print(c)
    return res

if __name__ == "__main__":
    p = 10
    a = 5

    sizes = [10 ** i for i in range(1, 7)]
    time_func_mean = []
    time_func_min = []
    time_func_max = []

    for size in sizes:
        b = random.randint(size, 10 * size)

        mean_func, min_func, max_func= measure_time(counter, b, p, a)
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
    plt.title("Выполнение counter")
    plt.legend()
    plt.grid(True)
    plt.show()
