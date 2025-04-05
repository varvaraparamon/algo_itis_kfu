from plot import *

def gray(x, n):
    res = x ^ (x >> 1)
    return format(res, f'0{n}b')

if __name__ == "__main__":

    sizes = [i for i in range(5, 15)]
    time_func_mean = []
    time_func_min = []
    time_func_max = []

    for n in sizes:
        x = random.randint(2^(n-1), 2^n - 1)

        mean_func, min_func, max_func= measure_time(gray, x, n)
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