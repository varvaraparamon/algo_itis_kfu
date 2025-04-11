"""
1. Дана строка, составленная из круглых скобок. Составить процедуру,
определяющую наименьшее количество символов, которые необходимо удалить из
этой строки, чтобы оставшиеся символы образовывали правильную скобочную
последовательность (ПСП). (Сложность O(n))
"""
res = 0
def count_scob(str):
    global res
    open_count, removals = 0, 0
    for symb in str:
        if symb == "(":
            open_count += 1
        elif symb == ")":
            if open_count >= 1:
                open_count -= 1
            else:
                removals += 1
    res = open_count + removals

if __name__ == "__main__":
    count_scob("hello((((()) sdfafas")
    print(res)
    count_scob("())))))))")
    print(res)