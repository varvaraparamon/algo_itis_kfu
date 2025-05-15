"""
Дана квадратная таблица a[0..n-1][0..n-1] и число mn. Для каждого
квадрата m×m в этой таблице вычислить сумму стоящих в нем чисел. Общее
число действий порядка O(n^2)
"""

import timeit

def compute_prefix_sum(a):
    n = len(a)
    p = []
    for i in range(n+1):
        p.append([0]*(n+1))
    for i in range(1, n):
        for j in range(1, n):
            p[i][j] = a[i-1][j-1] + p[i-1][j] + p[i][j-1] - p[i-1][j-1]
    return p

def sum_squares(a, m):
    a_copy = a.copy()
    for line in a_copy: 
        line.append(0)
    n = len(a_copy)
    a_copy.append([0]*(n+1))
    n = n+1
    p = compute_prefix_sum(a_copy)
    res = []
    for i in range(n-m):
        for j in range(n-m):
            res.append(p[i + m][j + m] - p[i][j + m] - p[i + m][j] + p[i][j])
    return res

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(sum_squares(a, 2))
print(timeit.timeit(lambda : sum_squares(a, 2), number=1000)/1000)