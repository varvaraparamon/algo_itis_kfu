"""
В массиве каждый элемент равен 0,1 или 2. Переставить элементы
массива так, чтобы сначала шли все нули, потом единицы и двойки.
Дополнительного массива не заводить. Посчитать временную сложность
предлагаемого решения. (Сложность )
"""

import timeit

def my_sort(a):
    low = 0
    mid = 0
    high = len(a) - 1

    while mid <= high:
        if a[mid] == 0:
            a[mid], a[low] = a[low], a[mid]
            mid += 1
            low += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    return a

a = [0,1,1,0,1,2,1,2,0,0,0,1]
print(my_sort(a))
print(timeit.timeit(lambda : my_sort(a), number=1000)/1000)