"""Выведите таблицу размером 𝑛×𝑛, заполненную числами от 1 до 𝑛2
по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь 𝑛=5):
"""

n = int(input())
arr = [[None for i in range(n)] for j in range(n)]
i = 0
j = 0
x = 1
y = 0
while x <= n**2:
    arr[i][j] = x
    if i != j:
        arr[j][i] = (arr[y][y] + (n - y * 2) * 2) * 2 - 4 - x
    if j != n - y -1:
        j += 1
    elif i != n - y -1:
        i += 1
    elif x != n**2:
        y +=1
        i,j = y, y
        x = arr[y][y-1]
    x += 1

for i in arr:
    print (*i)
