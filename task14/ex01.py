"""
Напишите рекурсивную программу для изменения на обратный порядка
следования узлов в линейном списке. (Сложность O(n)).
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

    def __repr__(self):
        return f'Node({self.value})'
    
    def print_list(head):
        current = head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

def reverse(head):
    if not head or not head.next:
        return head
    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head

import time
import numpy as np
def measure_time(func, *args, repeats=100):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

reverse(head).print_list()
print(measure_time(reverse, head))