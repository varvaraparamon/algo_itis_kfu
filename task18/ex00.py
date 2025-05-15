"""
Даны два возрастающих массива x: array[0..k-1] of integer и y: array[0..l1] of integer. Найти количество общих элементов в этих массивах, то есть
количество тех целых t, для которых t = x[i] = y[j] для некоторых i и j. (Число
действий порядка O(k + l).)
"""

import timeit

def find_common(x, y):
    i, j = 0, 0
    count = 0
    while i < len(x) and j < len(y):
        if x[i] == y[j]:
            i += 1
            j += 1
            count += 1
        elif x[i] < y[j]:
            i += 1
        else:
            j += 1
    return count

a = [1, 3, 5, 6, 7, 8, 9]
b = [2, 3, 5, 7]

print(find_common(a, b))
print(timeit.timeit(lambda : find_common(a, b), number=1000)/1000)