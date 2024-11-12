from itertools import permutations
n = int(input())
weak = list(map(int,input().split()))
dist = list(map(int,input().split()))

length = len(weak)
for i in range(length):
    weak.append(weak[i]+n)

def solution (n, weak, dist):
    max_cnt = len(dist)+1       
    friends = list(permutations(dist,len(dist)))
    for start in range(length):              
        for fr in friends:  
            cnt = 1
            ptr = weak[start]+fr[cnt-1]
            for i in range(start,start+length):
                if ptr < weak[i]:
                    cnt+=1
                    if cnt > len(dist):
                        break
                ptr = weak[i]+fr[cnt-1]
                #print(f'start={start},dist={fr[cnt-1]},ptr={ptr},cnt={cnt}')                
            newcnt=min(cnt,max_cnt)
        ans=min(newcnt,max_cnt)            
    return ans

#solution(n, weak,dist)
print(solution(n, weak,dist))