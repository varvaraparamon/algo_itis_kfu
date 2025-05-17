"""
Имеется массив из n чисел от 0 до 2^k -1, каждое из которых мы будем
рассматривать как k-битовое слово из нулей и единиц. Используя проверки «iый бит равен 0» и «i-ый бит равен 1» вместо сравнений, отсортировать все
числа за время порядка nk.
"""
import timeit

def radix_sort_bit(arr, k):
    for i in range(k):
        zeros = []
        ones = []

        for j in range(len(arr)):
            if (arr[j] >> i) & 1 == 0:
                zeros.append(arr[j])
            else:
                ones.append(arr[j])
            
        arr = zeros + ones
    return arr

x = [65, 1020, 3, 4, 100, 98, 2000]

print(radix_sort_bit(x, 11))
print(timeit.timeit(lambda : radix_sort_bit(x, 11), number=1000)/1000)