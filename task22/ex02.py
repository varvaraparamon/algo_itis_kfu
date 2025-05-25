"""
Даны n кругов, заданных своими центрами и радиусами. Постройте
алгоритм, который за O(n log n) определяет пересекаются (имеют общую точку)
хотя бы два из них.
"""

import math
import timeit

def check_circle_intersections(circles):
    events = []
    
    for i, (x, y, r) in enumerate(circles):
        events.append((x - r, 'start', i))
        events.append((x + r, 'end', i))
    

    events.sort(key = lambda x: (x[0], 0 if x[1] == 'start' else 1))
    active = []

    for event in events:
        xi, yi, ri = circles[event[2]]
        if event[1] == 'start':
            for yj, j in active:
                xj, yj, rj = circles[j]
                if abs(yi - yj) > ri + rj:
                    break

                d = math.sqrt((xi - xj)**2 + (yi - yj)**2)
                if d <= ri + rj:
                    return True
                
            active.append((yi, i))
            active.sort(key=lambda x: x[0])

        if event[1] == 'end':
            active.remove((yi, i))
    return False


circles = [
    (1, 2, 1),   
    (3, 4, 1),   
    (1.5, 2, 1)  
]

print(check_circle_intersections(circles))  
print(timeit.timeit(lambda : check_circle_intersections(circles), number=1000)/1000)