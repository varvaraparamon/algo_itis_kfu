"""
Фишка может двигаться по полю длины N только вперед. Длина хода фишки
не более K. Найти число различных путей, по которым фишка может пройти поле
от позиции 0 до позиции N - 1. Входными параметрами являются числа N и K
(Сложность по памяти O(K))
"""
import timeit

def findpaths(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    dp = [0]*n
    window = [1]
    cur_sum = 1
    res = 0

    for i in range(1, n):
        dp_i = cur_sum
        res = dp_i
        window.append(dp_i)
        cur_sum += dp_i

        if len(window) > k:
            deleted_el = window.pop(0)
            cur_sum -= deleted_el

    return res

print(findpaths(5, 2))
print(timeit.timeit(lambda : findpaths(5, 2), number=1000)/1000)

