from plot import *
"""
Даны две непустые очереди. Элементы каждой из очередей упорядочены по
возрастанию. Объединить очереди в одну с сохранением упорядоченности
элементов
ВАРИАНТ С ОЧЕРЕДЬЮ С ИСПОЛЬЗОВАНИЕМ СТЕКОВ
"""
class QueueUsingStacks:
    def __init__(self, _list = []):
        self.stack_in = _list
        self.stack_out = []

    def enqueue(self, value):
        """Добавить элемент в очередь"""
        self.stack_in.append(value)

    def dequeue(self):
        """Удалить и вернуть первый элемент"""
        if not self.stack_out:
            if not self.stack_in:
                raise IndexError("Очередь пуста")
            # Перемещаем все элементы из stack_in в stack_out
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        """Посмотреть первый элемент без удаления"""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("Очередь пуста")
        return self.stack_out[-1]

    def is_empty(self):
        """Проверка: очередь пуста?"""
        return not self.stack_in and not self.stack_out

    def __str__(self):
        """Строковое представление: как элементы будут извлекаться"""
        return str(self.stack_out[::-1] + self.stack_in)
    

def merge_queue_using_stacks(q1, q2):
    q = QueueUsingStacks()
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
    # q1 = QueueUsingStacks([1, 3, 5, 7, 9, 11])
    # q2 = QueueUsingStacks([1, 2, 4, 6])
    # print(merge_queue_using_stacks(q1, q2))
    sizes = [10 ** i for i in range(1, 7)]
    time_func_mean = []
    time_func_min = []
    time_func_max = []

    for size in sizes:
        b = QueueUsingStacks(sorted([random.randint(1, 1000) for i in range(size)])) 
        a = QueueUsingStacks(sorted([random.randint(1, 1000) for i in range(size)])) 

        mean_func, min_func, max_func= measure_time(merge_queue_using_stacks, a, b)
        time_func_mean.append(mean_func)
        time_func_min.append(min_func)
        time_func_max.append(max_func)

    plt.figure(figsize=(12, 6))

    plt.plot(sizes, time_func_mean, label="merge_queue_using_stacks", marker='o', color='blue')

    plt.fill_between(sizes, time_func_min, time_func_max, alpha=0.2, color='blue')

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Размер чисел")
    plt.ylabel("Время выполнения (секунды)")
    plt.title("Выполнение merge_queue_using_stacks")
    plt.legend()
    plt.grid(True)
    plt.show()