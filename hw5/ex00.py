"""
1. Реализуйте процедуру обхода в глубину в заданном
неориентированном графе (Сложность О(|Е|+|V|)
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item) 

    def pop(self):
        """ Удалить и вернуть верхний элемент стека """
        if self.is_empty():
            return None
        return self.stack.pop()  

    def peek(self):
        """Вернуть элемент с вершины стека без удаления. Если стек пуст, вернуть None"""
        if self.is_empty():
            return None
        return self.stack[-1] 

    def is_empty(self):
        """Проверить на пустоту"""
        return not self.stack

    def size(self):
        """Вернуть размер"""
        return len(self.stack)

    def __repr__(self):
        """Вернуть строковое представление стека."""
        return str(self.stack)

def dfs(graph, start):
    s = Stack()
    s.push(start)
    visited = {el : 0 for el in graph.keys()}
    visited[start] = 1

    while not s.is_empty():
        start = s.pop()
        for v in graph[start]:
            if visited[v] == 0 :
                visited[v] = 1
                s.push(v)

    return visited


graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
graph.keys

print(dfs(graph, 'A'))