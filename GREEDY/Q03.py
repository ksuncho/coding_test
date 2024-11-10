#https://www.acmicpc.net/problem/1439
array = input()
result = [array[0]]
for i in range(1,len(array)):
    if array[i]==array[i-1]:
        continue
    else:
        result.append(array[i])

cnt0=0
cnt1=0
for i in result:
    if i == '0':
        cnt0+=1
    else:
        cnt1+=1
print(result)
print(min(cnt0,cnt1))