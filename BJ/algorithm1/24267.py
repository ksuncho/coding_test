# sigma((k-2)*(k-1)/2)
# sigma k**2 = (n)*(n+1)*(2*n+1)/6
# sigma k = (n)*(n+1)/2
# sigma 2 = 2*n
# sigma((k-2)*(k-1)/2) = (2*n**3-6*n**2+4*n)/12
def MenOfPassion(A, n):
    sum = 0
    cnt = 0
    for i in range(1,n-1):
        for j in range(i+1,n):
            for k in range(j+1,n+1):
                sum += A[i] * A[j] * A[k] # 코드1
                cnt +=1
                print(i,j,k)
    return cnt
n = int(input())
print((2*n**3-6*n**2+4*n)//12)
print(3)