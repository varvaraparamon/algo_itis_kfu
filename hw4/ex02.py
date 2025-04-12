from plot import *
"""
3. В отсортированном списке удалить все дубликаты (Сложность O(n)).
Замерить время работы программы (запустить функцию не менее 10 раз и
посчитать среднее время работы) и построить график зависимости времени
работы от р
"""

def remove_dublicates(l):
    len_ = len(l)
    i = 0
    while i < len_-1:
        if l[i] == l[i+1]:
            l.pop(i)
            len_ -= 1
        else:
            i += 1

    return l

if __name__ == "__main__":
    # print(remove_dublicates([1, 2, 2, 3, 4, 4, 5, 6, 6, 6]))
    ls = [sorted([random.randint(1, 100) for i in range(x)]) for x in range(5, 20)]

    time_func_mean = []
    time_func_min = []
    time_func_max = []
    for l in ls:
        mean_func, min_func, max_func= measure_time(remove_dublicates, l)
        time_func_mean.append(mean_func)
        time_func_min.append(min_func)
        time_func_max.append(max_func)

    plt.figure(figsize=(12, 6))

    plt.plot(range(5, 20), time_func_mean, label="my_sqrt", marker='o', color='blue')

    plt.fill_between(range(5, 20), time_func_min, time_func_max, alpha=0.2, color='blue')

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Размер чисел")
    plt.ylabel("Время выполнения (секунды)")
    plt.title("Выполнение counter")
    plt.legend()
    plt.grid(True)
    plt.show()