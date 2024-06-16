def MenOfPassion(A, n):
    sum = 0
    cnt = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                sum += A[i] * A[j] * A[k] # 코드1
                cnt +=1
    return cnt
n = int(input())
#print(MenOfPassion([0]*(n),n))
print(MenOfPassion([0]*(n),n))
print(3)