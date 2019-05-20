a = input()
a = a.upper()
CG = a.count('G') + a.count('C')
percents = CG / len(a) * 100
print (percents)