"""
1. Написать функцию, которая слова в текстовом файле распечатывает в
обратном порядке. По файлу можно пройти только один раз (Сложность O(n)).
Можно реализовать с использованием стека
"""

def desc(filename):
    words = []
    with open(filename, 'r') as f:
        for line in f:
            words.extend(line.strip().split())

    while words:
        print(words.pop(), end= ' ')
    print("\n")

if __name__ == "__main__":
    desc("example.txt")