"""
Дан массив x: array[1..n] of integer. Найти количество различных чисел
среди элементов этого массива. (Число действий должно быть порядка O(nlogn)
"""
import timeit
import random

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)
    
a = [10, 3, 4, 2, 2 ]

def distinct(a):
    a = quicksort(a)
    distinct_count = 1
    for i in range(2, len(a)):
        if a[i] != a[i-1]:
            distinct_count += 1
    return distinct_count
print(distinct(a))
print(timeit.timeit(lambda: distinct(a), number=1000)/1000)
