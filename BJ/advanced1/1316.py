N = int(input())
count = 0
for i in range(N):
    words = [x for x in input()]
    j=0
    while True:
        if j > len(words)-1:
            break
        elif j == 0:
            words_x = list(words[j])
            j +=1
        else:
            if words[j] != words[j-1]:
                words_x.append(words[j])
            j +=1
    if len(words_x) == len(set(words)):
        count+=1
print(count)
print(words_x,set(words))
        

    
