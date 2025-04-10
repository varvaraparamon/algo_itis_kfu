"""
2. Для заданного числового массива а для каждого элемента a[i] найти
индекс ближайшего меньшего элемента. Если такого элемента нет - вернуть 0.
(Сложность O(n))
"""

def nearest_min(mas):
    n = len(mas)
    stack = []
    res = [0]*n
    for i in range(n):
        while stack and (mas[i] <= mas[stack[-1]]):
            stack.pop()
        
        if stack:
            res[i] = stack[-1] + 1
        
        stack.append(i)
    return res

if __name__ == "__main__":
    print(nearest_min([4, 7, 4, 5, 6, 3, 1, 9, 8]))
