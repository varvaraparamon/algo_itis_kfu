"""
Дана последовательность целых чисел x[1], . . . , x[n]. Найти
максимальную длину её возрастающей подпоследовательности (число
действий порядка n log n).
"""
import timeit

def lis_length(x):
    tails = []
    for i in range(len(x)):
        l = 0
        r = len(tails)
        while l < r:
            m = (l+r)//2
            if tails[m] < x[i]:
                l = m + 1
            else:
                r = m
        if len(tails) == l:
            tails.append(x[i])
        else:
            tails[l] = x[i]
    return len(tails)

x = [3, 1, 2, 1, 8, 5, 6]

print(lis_length(x))
print(timeit.timeit(lambda : lis_length(x), number=1000)/1000)