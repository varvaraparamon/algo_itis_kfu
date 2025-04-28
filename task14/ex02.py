"""
Реализуйте алгоритмы обхода вершин дерева в прямом порядке, внутренним
порядке, обратном порядке. (Сложность O(n)). 
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order(node):
    if node:
        print(node.value, end = " ")
        pre_order(node.left)
        pre_order(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value, end = " ")

def in_order(node):
    if node:
        in_order(node.left)
        print(node.value, end = " ")
        in_order(node.right)

import time
import numpy as np
def measure_time(func, *args, repeats=100):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times)


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

pre_order(tree)
print()
post_order(tree)
print()
in_order(tree)
print()

print(measure_time(pre_order, tree))
print(measure_time(post_order, tree))
print(measure_time(in_order, tree))