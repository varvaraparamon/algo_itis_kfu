"""
Дано n точек на плоскости. Указать (n − 1)-звенную несамопересекающуюся
незамкнутую ломаную, проходящую через все эти точки. (Соседним отрезкам
ломаной разрешается лежать на одной прямой (допускаются коллинеарные
точки)) Число действий порядка n log n
"""
import matplotlib.pyplot as plt
import timeit

def build_polyline(points):
    sorted_points = sorted(points, key = lambda x: (x[0], x[1]))
    plt.plot([x[0] for x in sorted_points], [x[1] for x in sorted_points])
    plt.show()

points = [(1, 2), (3, 1), (2, 2), (0, 0)]
build_polyline(points)
print(timeit.timeit(lambda x: build_polyline(points), number=1000)/1000)



    