"""
Записать в виде рекурсивной процедуры программу нахождения НОД двух
чисел
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    

import time
import numpy as np
def measure_time(func, *args, repeats=100):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times)

if __name__ == "__main__":

    print(gcd(80, 25))
    print(measure_time(gcd, 80, 25))