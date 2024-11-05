array = [int(i) for i in str(input())]
result = array[0]
for i in range(1,len(array)):
    if result<=1 or array[i] <= 1:
        result += array[i]
    else:
        result *= array[i]

print(result)