"""
Реализовать алгоритм лексикографической сортировки для векторов
переменной длины, элементы которых принимают значения из конечного
алфавита А. Сложность O(mk), где m – число всех векторов, k – длина
максимального из них. 
"""

import timeit

def msd_radix_sort(strings, d):
    if len(strings) <= 1:
        return strings
    buckets = {}
    for s in strings:
        if d < len(s):
            char = s[d]
        else:
            char = ' '

        if char not in buckets:
            buckets[char] = []
        buckets[char].append(s)
    sorted_strings = []
    for char in sorted(buckets.keys()):
        sorted_strings.extend(msd_radix_sort(buckets[char], d + 1))
    return sorted_strings

strings = ["ba", "abc", "ab", "b"]
print(msd_radix_sort(strings, 0))
print(timeit.timeit(lambda: msd_radix_sort(strings, 0), number=1000)/1000)