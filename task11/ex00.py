from collections import deque
from plot import *
"""
Даны две непустые очереди. Элементы каждой из очередей упорядочены по
возрастанию. Объединить очереди в одну с сохранением упорядоченности
элементов
ВАРИАНТ С DEQUE
"""
class QueueDeque:
    def __init__(self, _list = []):
        self.d = deque(_list)
    def enqueue(self, el):
        self.d.append(el)
    def dequeue(self):
        if not self.d:
            raise IndexError("Очередь пуста")
        return self.d.popleft()
    def peek(self):
        if not self.d:
            raise IndexError("Очередь пуста")
        return self.d[0]
    def is_empty(self):
        return not self.d
    def __repr__(self):
        return str(self.d)
    

def merge_deque(q1, q2):
    q = QueueDeque()
    while not q1.is_empty() and not q2.is_empty():
        if q1.peek() <= q2.peek():
            q.enqueue(q1.dequeue())
        else:
            q.enqueue(q2.dequeue())
    if not q1.is_empty():
        while not q1.is_empty():
            q.enqueue(q1.dequeue())
    elif not q2.is_empty():
        while not q2.is_empty():
            q.enqueue(q2.dequeue())
    return q

if __name__ == "__main__":
    # q1 = QueueDeque([1, 3, 5, 7, 9, 11])
    # q2 = QueueDeque([1, 2, 4, 6])
    # print(merge_deque(q1, q2))
    sizes = [10 ** i for i in range(1, 7)]
    time_func_mean = []
    time_func_min = []
    time_func_max = []

    for size in sizes:
        b = QueueDeque(sorted([random.randint(1, 1000) for i in range(size)])) 
        a = QueueDeque(sorted([random.randint(1, 1000) for i in range(size)])) 

        mean_func, min_func, max_func= measure_time(merge_deque, a, b)
        time_func_mean.append(mean_func)
        time_func_min.append(min_func)
        time_func_max.append(max_func)

    plt.figure(figsize=(12, 6))

    plt.plot(sizes, time_func_mean, label="merge_deque", marker='o', color='blue')

    plt.fill_between(sizes, time_func_min, time_func_max, alpha=0.2, color='blue')

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Размер чисел")
    plt.ylabel("Время выполнения (секунды)")
    plt.title("Выполнение merge_deque")
    plt.legend()
    plt.grid(True)
    plt.show()
