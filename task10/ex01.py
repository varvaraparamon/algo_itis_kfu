"""
Напишите процедуру реализации очереди с использованием двух стеков.
Оцените сложность такого моделирования
"""

class Queue:
    def __init__ (self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self, x):
        self.s1.append(x)
    
    def dequeue(self):
        if not self.s2:
            if not self.s1:
                raise IndexError("queue is empty")
            while (self.s1):
                self.s2.append(self.s1.pop())

        return self.s2.pop()
    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  
    print(q.dequeue())  
    q.enqueue(4)
    print(q.dequeue())  
    print(q.dequeue())  

