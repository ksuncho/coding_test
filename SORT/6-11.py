N = int(input())
array = []
for i in range(N):
    input_data = input().split()
    array.append((input_data[0],input_data[1]))
#my answer
#if 1
def setting(A):
    return A[1]
array = sorted(array,key=setting)
#else
#book's answer
#array = sorted(array, key=lambda student:student[1])
#endif

for i in array:
    print(i[0], end=' ')