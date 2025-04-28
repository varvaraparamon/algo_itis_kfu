import numpy as np
import os

def generate_random_graph(size, density=0.5, max_weight=10):
    graph = np.full((size, size), np.inf)
    np.fill_diagonal(graph, 0)  
    
    for i in range(size):
        for j in range(size):
            if i != j and np.random.random() < density:
                weight = np.random.randint(1, max_weight + 1)
                graph[i][j] = weight
                
    return graph

def save_graphs_to_files(start=10, end=100):
    if not os.path.exists("graphs"):
        os.makedirs("graphs")
        
    for size in range(start, end + 1):
        graph = generate_random_graph(size)
        filename = f"graphs/graph_{size}x{size}.txt"
        np.savetxt(filename, graph, fmt='%f')
        print(f"Сгенерирован и сохранён граф размером {size}x{size}")

save_graphs_to_files()