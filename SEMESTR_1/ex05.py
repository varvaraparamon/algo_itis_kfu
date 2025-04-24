"""
Вводится из файла список строк. Вводится подстрока. Определить индексы элементов списка в которых содержится подстрока без учета регистра.
"""

substring = input().lower()

with open("ex05.txt", "r") as file:
    lines = [line.lower() for line in file]

    for i, line in enumerate(lines):
        if substring in line:
            print(i)