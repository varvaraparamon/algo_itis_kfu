"""
Постройте эффективный алгоритм, который определяет, есть ли в
данном ориентированном графе вершина, из которой достижимы все
вершины графа.
"""
import timeit

def find_vertex(g):
    visited = [False]*len(g)
    candidate = None

    for v in range(len(g)):
        if not visited[v]:
            DFS(g, v, visited)
            candidate = v

    for i in range(len(g)):
        visited[i] = False

    DFS(g, candidate, visited)

    for v in range(len(g)):
        if not visited[v]:
            return None
    
    return candidate

def DFS(g, v, visited):
    stack = [v]

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
        
        for neighbour in reversed(g[vertex]):
            if not visited[neighbour]:
                stack.append(neighbour)


g = { 
    0 : [1],
    1 : [2],
    2 : [3],
    3 : []
}

print(find_vertex(g))
print(timeit.timeit(lambda : find_vertex(g), number=1000)/1000)