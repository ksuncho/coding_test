#https://school.programmers.co.kr/learn/courses/30/lessons/60057#
array = str(input())
length = len(array)
minsize = length
for size in range(1,length//2+1):
    prev=''
    data=''
    cnt = 0
    ccnt = 0
    while ccnt < len(array)/size:
        if ccnt*size+size < length:
            cur = array[ccnt*size:ccnt*size+size]
            if cur==prev:
                cnt+=1
            else:
                if cnt!=0:
                    data=data+str(cnt+1)+prev
                else:
                    data=data+prev
                cnt=0
            prev=cur    
        else:
            cur = array[ccnt*size:]
            if cur==prev:
                cnt+=1
                data=data+str(cnt+1)+prev
            else:
                if cnt!=0:     
                    data=data+str(cnt+1)+prev+cur
                else:
                    data=data+prev+cur    
        ccnt+=1
    csize=len(data)
    print(f'size={size}:data={data},size={csize}')
    if csize<=minsize:
        minsize=csize
print(minsize)
