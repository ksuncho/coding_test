array = str(input())
alphabet=[]
number=0
for i in array:
    if ord(i)>=65:
        alphabet.append(i)        
    else:
        number+=int(i)
alphabet.sort()
if number!=0:
    alphabet.append(str(number))
print(''.join(alphabet))