"""
Напишите рекурсивную процедуру вычисления log N!
"""
import math

def my_log(n):
    if n == 0 or n == 1:
        return 0
    else:
        return math.log(n) + my_log(n-1)
    

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
    
print(my_log(5))
print(measure_time(my_log, 5))