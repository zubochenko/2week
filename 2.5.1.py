x = input()
x = list((x.split()))
new_list = []
for _ in x:
    new_list.append(int(_))
print (sum(new_list))