"""
Имеется квадратная таблица a. Известно, что для некоторого i строка
с номером i заполнена одними нулями, а столбец с номером i — одними
единицами (за исключением их пересечения на диагонали, где стоит
неизвестно что). Найти такое i (оно, очевидно, единственно). Число
действий порядка n. (Заметим, что это существенно меньше числа
элементов в таблице).
"""
import timeit

def find_i(a):
    n = len(a)
    candidate = 0

    for i in range(1, n):
        if a[candidate][i] == 1 or a[i][candidate] == 0:
            candidate = i
    
    for j in range(n):
        if j != candidate and a[candidate][j] != 0:
            return None
    
    for i in range(n):
        if i != candidate and a[i][candidate] != 1:
            return None
        
    return candidate


a = [
 [0, 1, 1, 1],
 [0, 0, 0, 0],
 [0, 1, 0, 1],
 [0, 1, 1, 0]
]

print(find_i(a))
print(timeit.timeit(lambda : find_i(a), number=1000)/1000)