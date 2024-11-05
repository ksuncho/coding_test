array = input()
result = []
for i in range(1,len(array)):
    if array[i]==array[i-1]:
        continue
    else:
        result.append(array[i])

cnt0=0
cnt1=1
for i in result:
    if i == '0':
        cnt0+=1
    else:
        cnt1+=1

print(min(cnt0,cnt1))