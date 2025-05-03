"""
Даны два двоичных дерева. Написать эффективную процедуру, которая
проверяет их изоморфизм.
"""
from ex00 import measure_time
from ex01 import TreeNode

def is_isomorfic(n1, n2):
    if not n1 and not n2:
        return True
    elif not n1 or not n2:
        return False
    elif n1.value != n2.value:
        return False
    
    return (is_isomorfic(n1.left, n2.left) and is_isomorfic(n1.right, n2.right)) or \
           (is_isomorfic(n1.left, n2.right) and is_isomorfic(n1.right, n2.left))
    
if __name__ == "__main__":

    # Representation of input binary tree 1
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    #       / \
    #      7   8
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(8)

    # Representation of input binary tree 2
    #        1
    #       / \
    #      3   2
    #     /   / \
    #    6   4   5
    #           / \
    #          8   7
    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(6)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(5)
    root2.right.right.left = TreeNode(8)
    root2.right.right.right = TreeNode(7)

    if is_isomorfic(root1, root2):
        print("True")
    else:
        print("False")

    print(measure_time(is_isomorfic, root1, root2))