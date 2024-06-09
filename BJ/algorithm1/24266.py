def MenOfPassion(A, n):
    sum = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                sum += A[i] * A[j] * A[k] # 코드1
    return sum
n = int(input())
print(n**3)
print(3)