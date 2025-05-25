"""
В множестве Q рассмотрим две наиболее удаленные точки. Покажите, что
каждая из них входит в выпуклую оболочку.
"""

import math
import timeit

def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def find_farthes_points(q):
    ch = graham_scan(q)

    max_dist = 0
    best_pair = (0, 0)
    j = 1

    for i in range(len(ch)):
        while dist(ch[i], ch[(j+1)%len(ch)]) > dist(ch[i], ch[j]):
            j = (j + 1) % len(ch) 
        d = dist(ch[i], ch[j])

        if d > max_dist:
            max_dist = d
            best_pair = (ch[i], ch[j])
    return best_pair


from math import atan2
def cross(o, a, b):
    return (a[0] - o[0])*(b[1] - o[1]) - (a[1] - o[1])*(b[0] - o[0])

def graham_scan(points):
    start = min(points, key=lambda p: (p[1], p[0]))
    def polar(p):
        return atan2(p[1] - start[1], p[0] - start[0])

    sorted_points = sorted(points, key=lambda p: (polar(p), (p[0]-start[0])**2 + (p[1]-
    start[1])**2))
    stack = []
    for p in sorted_points:
        while len(stack) >= 2 and cross(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)
    return stack


points = [(0,0), (1,1), (2,2), (2,0), (0,2), (1,0.5)]
print(find_farthes_points(points))
print(timeit.timeit(lambda : find_farthes_points(points), number=1000)/1000)