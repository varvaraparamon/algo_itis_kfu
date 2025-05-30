"""
Покажите, как за время o nlogn удалить из массива размерности n все
дубликаты.
"""
import timeit
def merge_sort(a):
    if len(a) <= 1:
        return
    mid = len(a)//2
    left_half = a[:mid]
    right_half = a[mid:]
    merge_sort(left_half)
    merge_sort(right_half)

    i, j, k = 0, 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            a[k] = left_half[i]
            i += 1
        else:
            a[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        a[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        a[k] = right_half[j]
        j += 1
        k += 1
    return a

def delet_dups(a):
    if len(a) <= 1:
        return a
    a = merge_sort(a)
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            res.append(a[i])
    return res

a =  [4, 2, 7, 4, 2, 9]

print(delet_dups(a))
print(timeit.timeit(lambda : delet_dups(a), number=1000)/1000)