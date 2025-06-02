"""
Дан ориентированный ациклический граф G = (V, E) и две вершины s и t.
Требуется найти количество различных путей из s в t за O(|V| + |E|) с
использованием динамического программирования.
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

def count_paths_dag(g, s, t):
    dp = [0]*len(g)
    dp[s] = 1
    order = topological_sort(g)

    for u in order:
        for neigbour in g[u]:
            dp[neigbour] += dp[u]
    return dp[t]

g = {
    0 : [1, 3],
    1: [2], 
    2 : [4], 
    3 : [4],
    4 : []
}
print(count_paths_dag(g, 0, 4))