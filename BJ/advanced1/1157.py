import sys
words = list(x for x in str(sys.stdin.readline().rstrip()).upper())
unique_words = set(words)
max = 0
max_word = 0
xx = []
for i in unique_words:
    count = 0
    for j in words:
        if i==j:
            count +=1
    if count > max:
        max = count
        max_word = i
    xx.append(count)
xx.sort()
if len(xx) >= 2:
    if xx[-1]==xx[-2]:
        print('?')
    else:
        print(max_word)
else:
    print(max_word)
print(xx)