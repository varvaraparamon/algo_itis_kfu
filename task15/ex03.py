"""
Для каждого узла двоичного дерева найти высоту поддерева, с корнем в
заданном узле.
"""

from ex00 import measure_time

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0 

def calculate_height(node):
    if not node:
        return 0
    left = calculate_height(node.left)
    right = calculate_height(node.right)
    node.height = 1 + max(left, right)
    return node.height

def print_preorder(node):
    if node:
        print(f"Узел {node.value}: высота = {node.height}")
        print_preorder(node.left)
        print_preorder(node.right)
a = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
a.left = b
a.right = c
b.left = d
b.right = e
time = measure_time(calculate_height, a)
print_preorder(a)
print(time)