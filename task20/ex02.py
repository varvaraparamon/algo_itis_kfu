"""
Дано n различных по весу камней и число k (от 1 до n). Требуется найти
k-ый по весу камень, сделав не более Cn взвешиваний, где C — некоторая
константа, не зависящая от k и n.
"""
import timeit
import math

def select(stones, k):
    n = len(stones)
    
    if n <= 5:
        sorted_stones = sorted(stones)
        return sorted_stones[k - 1]
    
    groups = [stones[i:i+5] for i in range(0, n, 5)]
    
    medians = []
    for group in groups:
        sorted_group = sorted(group)
        m = len(sorted_group)
        medians.append(sorted_group[m // 2])
    
    median_of_medians = select(medians, math.ceil(len(medians) / 2))
    
    less = [stone for stone in stones if stone < median_of_medians]
    equal = [stone for stone in stones if stone == median_of_medians]
    greater = [stone for stone in stones if stone > median_of_medians]
    
    size_less = len(less)
    size_equal = len(equal)
    
    if k <= size_less:
        return select(less, k)
    elif k <= size_less + size_equal:
        return median_of_medians
    else:
        return select(greater, k - size_less - size_equal)
    

stones = [7, 2, 9, 4, 1, 5, 3, 6, 8]

print(select(stones, 4))
print(timeit.timeit(lambda : select(stones, 4), number=1000)/1000)