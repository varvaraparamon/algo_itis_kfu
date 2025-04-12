"""
2. Написать программу, которая определяет, является ли введенная
скобочная структура правильной. Примеры правильных скобочных выражений:
(), (())(), ()(), ((())), неправильных — )(, ())((), (, )))), ((()). (Сложность O(n))
"""

def count_scob(str):
    stack = []
    for elem in str:
        if elem == "(":
            stack.append(elem)
        elif elem == ")":
            if not stack:
                return False
            stack.pop()

    if not stack:
        return True
    else:
        return False
    

if __name__ == "__main__":
    print(count_scob("hello((((()) sdfafas"))
    print(count_scob("())))))))"))
    print(count_scob("()()"))