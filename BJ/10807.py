def countt(m,data,t):    
    count = 0
    if len(data) != m:
        return 0
    else:
        for i in data:
            if (i == t):
                count += 1
        return count

if __name__ == '__main__':
    m = int(input())
    data = list(map(int, input().split()))
    t = int(input())
    #m = 11
    #data = [1, 4, 1, 2, 4, 2, 4, 2, 3, 4, 4]
    ##t = 2
    print(countt(m,data,t))
    #print(data)