"""
Постройте линейный алгоритм, который определяет, есть ли в данном
ориентированном графе путь проходящий через каждую вершину ровно один
раз (задача о Гамильтоновом пути в ориентированном графе).
"""

import timeit

def DFS(g, v, visited, stack):
    visited[v] = True
    for neighbour in g[v]:
        if not visited[neighbour]:
            DFS(g, neighbour, visited, stack)
    stack.append(v)

def topological_sort(g):
    n = len(g)
    visited = [False] * n
    stack = []
    
    for v in range(n):
        if not visited[v]:
            DFS(g, v, visited, stack)
    
    return stack[::-1] 

def has_hamiltonian_path(g):
    top_order = topological_sort(g)
    
    for i in range(len(top_order) - 1):
        u = top_order[i]
        v = top_order[i + 1]
        if v not in g[u]:
            return False
    return True


G = {
 0: [1],
 1: [2],
 2: [3],
 3: []
}

print(has_hamiltonian_path(G))
print(timeit.timeit(lambda : has_hamiltonian_path(G), number=1000)/1000)