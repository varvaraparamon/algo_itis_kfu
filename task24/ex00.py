"""
Нахождение пары ближайших точек (для Евклидовой метрики) алгоритмом
разделяй и властвуй за O (N log N).
"""
import timeit

import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(points):
    min_dist = float('inf')
    best_pair = (None, None)
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                best_pair = (points[i], points[j])
    return (*best_pair, min_dist)

def closest_recursive(px, py):
    n = len(px)
    if n <= 3:
        return brute_force(px)
    
    mid = n // 2
    qx = px[:mid]
    rx = px[mid:]
    mid_x = px[mid][0]
    
    qy = [point for point in py if point[0] <= mid_x]
    ry = [point for point in py if point[0] > mid_x]
    
    (a1, b1, d1) = closest_recursive(qx, qy)
    (a2, b2, d2) = closest_recursive(rx, ry)
    
    if d1 < d2:
        d = d1
        best_pair = (a1, b1)
    else:
        d = d2
        best_pair = (a2, b2)
    
    sy = [point for point in py if abs(point[0] - mid_x) < d]
    for i in range(len(sy)):
        for j in range(i + 1, min(i + 7, len(sy))):
            current_dist = distance(sy[i], sy[j])
            if current_dist < d:
                d = current_dist
                best_pair = (sy[i], sy[j])
    
    return (*best_pair, d)

def closest_pair(points):
    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])
    return closest_recursive(px, py)

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
p1, p2, dist = closest_pair(points)
print(p1, p2, dist)

print(timeit.timeit(lambda : closest_pair(points), number=1000)/1000)