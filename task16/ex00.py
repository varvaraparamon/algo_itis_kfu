"""
Даны два отсортированных массива. Один длинной n, другой длиной m.
Определить медиану этих двух массивов в совокупности. 
"""

import timeit

def FindMedianSortedArrays(a, b):
    if len(a) > len(b):
        a, b = b, a
    n, m = len(a), len(b)
    low, high = 0, n
    totalLeft = (n+m+1)//2

    while low <= high:
        i = (low + high)//2
        j = totalLeft - i

        a_left = float('-inf') if i == 0 else a[i-1]
        a_right = float('inf') if i == n else a[i]

        b_left = float('-inf') if j == 0 else b[j-1]
        b_right = float('inf') if j == m else b[j]

        if a_left <= b_right and b_left <= a_right:
            if (n+m)//2 == 1:
                return max(a_left, b_right)
            else:
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            high = i-1
        else:
            low = i+1


a = [1, 2, 3, 4, 5, 8]
b = [3, 4, 5, 6, 7, 9]
print(FindMedianSortedArrays(a, b))
print(timeit.timeit(lambda : FindMedianSortedArrays(a, b), number=1000))