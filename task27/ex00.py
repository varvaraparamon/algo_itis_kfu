"""
В заданной числовой последовательности A[0..N-1] определить
максимальную длину подпоследовательности подряд идущих одинаковых
элементов. Требуется реализовать алгоритм со сложностью O(N), используя идею
динамического программирования.
"""

import timeit

def max_equal_sent(a):
    n = len(a)
    if n == 0:
        return 0
    
    cur_len = 1
    max_len = 1

    for i in range(1, n):
        if a[i] == a[i-1]:
            cur_len += 1
        else:
            cur_len = 1

        if cur_len > max_len:
            max_len = cur_len
    return max_len

print(max_equal_sent("abcaaaabbbbbbcccdddd"))
print(timeit.timeit(lambda : max_equal_sent("abcaaaabbbbbbcccdddd"), number=1000)/1000)