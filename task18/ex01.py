"""
Некоторое число содержится в каждом из трех целочисленных
неубывающих массивов x[0] . . . x[p-1], y[0] . . . y[q-1], z[0] . . . z[r-1]. Найти
одно из таких чисел. Число действий должно быть порядка O(p + q + r)
"""
import timeit

def find_common(x, y, z):
    i, j, k = 0, 0, 0
    while i < len(x) and j < len(y) and k < len(z):
        if x[i] == y[j] == z[k]:
            return x[i]
        
        m = min(x[i], y[j], z[k])

        if x[i] == m:
            i += 1
        elif y[j] == m:
            j += 1
        else:
            k += 1
    return -1

x = [1, 2, 4, 6, 8]
y = [3, 4, 7, 10]
z = [1, 2, 4, 111]

print(find_common(x, y, z))
print(timeit.timeit(lambda : find_common(x, y ,z), number=1000)/1000)

