"""
Для заданного бинарного дерева для каждого узла подсчитать число его
потомков. (Сложность O(n)).
"""

from ex00 import measure_time

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.descendants = 0

def count_descendants(node):
    if not node:
        return 0
    left = count_descendants(node.left)
    right = count_descendants(node.right)
    node.descendants = left + right 
    return node.descendants + 1

def print_preorder(node):
    if node:
        print(f"Узел {node.value}: потомков = {node.descendants}")
        print_preorder(node.left)
        print_preorder(node.right)

if __name__ == "__main__":
    a = TreeNode('A')
    b = TreeNode('B')
    c = TreeNode('C')
    d = TreeNode('D')
    e = TreeNode('E')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    # Подсчёт потомков
    time = measure_time(count_descendants, a)
    # Затем обходим дерево в прямом порядке и печатаем
    print_preorder(a)
    print(time)