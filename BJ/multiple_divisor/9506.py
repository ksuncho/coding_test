while True:
    n = int(input())
    if n == -1:
        break
    else:
        factor = [x for x in range(1,n) if (n%x==0)]
        if sum(factor)==n:
            print(f'{n} =',end=' ')
            for f in factor:
                if f==1:
                    print(f'{f}',end=' ')
                else:
                    print(f'+ {f}',end=' ')
        else:
            print(f'{n} is NOT perfect.')

