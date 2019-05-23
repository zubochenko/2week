"""Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме
 элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний
 элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению."""
mtrx = []
lst = []
x = 0
res = []
res_mtrx = []
while True:
    x = input()
    if x == "end":
        break
    lst = list((x.split()))
    lst = [int(_) for _ in lst]
    mtrx.append(lst)

for i in range(len(mtrx)):
    for j in range(len(mtrx[0])):
        res.append(mtrx[i-1][j] + mtrx[(i+1)%len(mtrx)][j] + mtrx[i][j-1] + mtrx[i][(j+1)%len(mtrx[0])])
def chunks(lst):
     chunk_size = int(len(lst) / 3)
     return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]
res_mtrx = chunks(res)
for i in res_mtrx:
    print (*i, end = '\n')