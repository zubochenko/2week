"""Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран
в одну строку значения, которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным."""
x = input()
x = list((x.split()))
nonunique_list = sorted(set([i for i in x if x.count(i)>1]))

print (*nonunique_list)