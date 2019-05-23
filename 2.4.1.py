word = input()
x = 1
word_2 = word[x:x+1]
b = 1

for i in word:
    if i in word_2:
        b +=1
    else:
        print (i, end = '')
        print (b, end = '')
        b = 1
    x += 1
    word_2 = word[x:x+1]

