"""
Покажите, что n отрезков могут иметь O(n^2) точек пересечения
"""

import matplotlib.pyplot as plt
import timeit

def generate_segments(n):
    k = n//2
    segments = []

    for i in range(k):
        x = i/k
        start = (x, 0)
        end = (x, 1)
        segments.append((start, end))
    
    for j in range(k):
        y = j/k
        start = (0, y)
        end = (1, y)
        segments.append((start, end))
    return segments

n = 4
print(timeit.timeit(lambda : generate_segments(n), number=1000)/1000)