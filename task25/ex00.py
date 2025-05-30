"""
Пусть задан числовой массив размерности n. Напишите рекурсивную
функцию поиска максимального элемента, используя подход «Разделяй и властвуй».
"""

import timeit

def find_max(a, left, right):
    if left == right:
        return a[left]
    
    mid = (left + right)//2

    return max(find_max(a, left, mid), find_max(a, mid + 1, right))

a = [3, 8, 2, 5, 1, 9, 7]
print(find_max(a, 0, len(a) - 1))
print(timeit.timeit(lambda : find_max(a, 0, len(a) - 1), number=1000)/1000)