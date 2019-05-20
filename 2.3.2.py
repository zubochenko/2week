a = int(input())
b = int(input())
c = []
for i in range(a, b+1):
    if i % 3==0:
        c.append(i)
print (sum(c)/len(c))
