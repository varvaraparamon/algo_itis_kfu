"""
Вводится из файла список строк. Вводится подстрока. 
Определить индексы элементов списка в которых содержится подстрока без учета регистра.(без использования библиотечных функций)
"""
def my_lower(str):
    lower_str = ""
    for s in str:
        if 'A' <= s <= 'Z':
            s = chr(ord(s) + 32) 
        lower_str += s
    return lower_str

substring = my_lower(input())

with open("ex05.txt", "r") as file:
    lines = [my_lower(line) for line in file]

    for i, line in enumerate(lines):
        if substring in line:
            print(i)

