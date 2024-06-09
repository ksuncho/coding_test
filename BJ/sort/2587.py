array = []
for i in range(5):
    array.append(int(input()))

array = sorted(array)
print(int(sum(array)/len(array)))
print(array[len(array)//2])