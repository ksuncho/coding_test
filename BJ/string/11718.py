#if 1
#my answer
while True:
    try:
        S = str(input())
        print(S)
    except:
        break
#else
#Other answer
while True:
    try:
        print(input())
    except EOFError:
        break