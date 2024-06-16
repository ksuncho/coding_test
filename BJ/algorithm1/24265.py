def MenOfPassion(A, n):
    #sum = 0
    cnt = 0
    for i in range(n-1):
        for j in range(i+1,n):
            #sum += A[i] * A[j] # 코드1
            cnt +=1
    return cnt
n = int(input())
print(n*(n-1)//2)
print(2)