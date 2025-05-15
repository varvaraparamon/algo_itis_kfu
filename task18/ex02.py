"""
Дан список неотрицательных чисел. Измените их порядок так, чтобы
если их после этого выписать в строку, то получилось максимальное из
возможных чисел. Пример: дан массив [3, 30, 34, 5, 9]. Максимальное возможное число можно
получить 9534330. Сложность O(n log n)
"""

import timeit

def compare(a, b):
    if a + b >= b + a:
        return 0
    return 1

def max_num(x):
    str_arr = []
    for num in x:
        str_arr.append(str(num))
    for i in range(len(str_arr)):
        for j in range(1, len(str_arr)):
            if compare(str_arr[j-1], str_arr[j]):
                str_arr[j-1], str_arr[j] = str_arr[j], str_arr[j-1]

    res = ''
    for s in str_arr:
        res += s
    if res[0] == '0':
        return '0'
    return res
        
print(max_num([3, 30, 34, 5, 9]))
print(timeit.timeit(lambda : max_num([3, 30, 34, 5, 9]), number=1000)/1000)