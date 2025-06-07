"""
Имеется k неделимых предметов. Для каждого предмета известна его
масса (в кг.). Величины массы являются натуральными числами. Определить,
существует ли несколько предметов, суммарная масса предметов которого ровно
S кг. Если такой набор существует, то требуется определить список предметов в
наборе. (Сложность O(S*k)).
"""

def find_sum(k, w, s):
    dp = []
    for i in range(k+1):
        dp.append([False]*(s+1))
    dp[0][0] = True

    for i in range(1, k+1):
        for j in range(s+1):
            if dp[i-1][j] == True:
                dp[i][j] = True
            elif (j >= w[i-1] and  dp[i-1][j - w[i-1]]):
                dp[i][j] = True
    if dp[k][s] == False:
        print("Набор с суммой S не существует")
        return
    subset = []
    i = k
    j = s
    while j>0 and i>0:
        if j >= w[i-1] and dp[i-1][j - w[i-1]] == True:
            subset.append(w[i-1])
            j = j - w[i-1]
            i = i - 1
        else:
            i = i - 1
    print(subset)

find_sum(4, [2,3,7,8], 11)