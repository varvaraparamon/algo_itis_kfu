import time
import numpy as np
import pandas as pd

def floyd_warshall(graph):
    n = len(graph)
    dist = np.array(graph, dtype=float) 

    iterations = 0
    start_time = time.perf_counter()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                iterations += 1
    end_time = time.perf_counter()
    return dist, end_time - start_time, iterations

def test():
    sizes = []
    times = []
    iterations_list = []

    results = []
    
    for size in range(10, 101):
        filename = f"graphs/graph_{size}x{size}.txt"
        graph = np.loadtxt(filename, dtype=float)
        
        _, exec_time, iterations = floyd_warshall(graph)
        
        results.append({
            'size': size,
            'time_sec': exec_time,
            'iterations': iterations
        })
        
        print(f"Размер: {size}x{size}, Время: {exec_time:.6f} сек, Итераций: {iterations}")

    df = pd.DataFrame(results)
    df.to_csv('floyd_warshall_results.csv', index=False)
    
    return df


df = test()

import matplotlib.pyplot as plt

def plot_results(df):

    sizes = df['size']
    times = df['time_sec']
    iterations = df['iterations']

    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(sizes, times, 'bo-')
    plt.title('Время выполнения алгоритма')
    plt.xlabel('Размер матрицы')
    plt.ylabel('Время (сек)')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(sizes, iterations, 'ro-')
    plt.title('Количество итераций')
    plt.xlabel('Размер матрицы')
    plt.ylabel('Итераций')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('floyd_warshall.png', dpi=300)
    plt.show()



plot_results(df)

# ПРИМЕР ИСПОЛЬЗОВАНИЯ
# graph = [
# [0, 3, 8, np.inf, -4],
# [np.inf, 0, np.inf, 1, 7],
# [np.inf, 4, 0, np.inf, np.inf],
# [2, np.inf, -5, 0, np.inf],
# [np.inf, np.inf, np.inf, 6, 0]
# ]
# shortest_paths = floyd_warshall(graph)
# print("Матрица кратчайших расстояний:")
# print(shortest_paths)