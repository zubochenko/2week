"""Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого
списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент,
находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается
список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом."""

x = input()
x = list((x.split()))
new_list = []
answer = []
for _ in x:
    new_list.append(int(_))
if len(new_list) > 1:
    for i in range(0, len(new_list)-1):
        answer.append(new_list[i-1] + new_list[i+1])
    answer.append(new_list[0]+new_list[-2])
else:
    answer = new_list
print (*answer)