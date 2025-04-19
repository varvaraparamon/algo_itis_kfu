"""
1. Реализуйте процедуру обхода в глубину в заданном
неориентированном графе (Сложность О(|Е|+|V|)
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item) 

    def dequeue(self):
        """ Удалить и вернуть верхний элемент"""
        if self.is_empty():
            return None
        return self.queue.pop(0)  

    def peek(self):
        """Вернуть элемент с вершины без удаления. Если пуст, вернуть None"""
        if self.is_empty():
            return None
        return self.queue[0] 

    def is_empty(self):
        """Проверить на пустоту"""
        return not self.queue

    def size(self):
        """Вернуть размер"""
        return len(self.queue)

    def __repr__(self):
        """Вернуть строковое представление."""
        return str(self.queue)

def bfs(graph, start):
    q = Queue()
    q.enqueue(start)
    visited = {el : 0 for el in graph.keys()}
    visited[start] = 1

    while not q.is_empty():
        start = q.dequeue()
        for v in graph[start]:
            if visited[v] == 0 :
                visited[v] = 1
                q.enqueue(v)

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

print(bfs(graph, 'A'))