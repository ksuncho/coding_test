# S = [x for x in str(input())]
# i = 0
# count = 0
# if len(S) >= 2:
#     while True:
#         if i >= len(S):
#             break
#         elif i == len(S)-1:
#             count +=1
#             i +=1
#         else:
#             print(i,S[i])
#             if S[i] == 'c':
#                 if (S[i+1] == '=') or (S[i+1] == '-'):
#                     i += 2
#                 else:
#                     i += 1
#             elif S[i] == 'd':
#                 if (S[i+1] == 'z'):
#                     i += 3
#                 elif (S[i+1] == '-'):
#                     i += 2
#                 else:
#                     i += 1
#             elif (S[i] == 'l') or (S[i] == 'n'):
#                 if (S[i+1] == 'j'):
#                     i += 2
#                 else:
#                     i += 1
#             elif (S[i] == 's') or (S[i] == 'z'):
#                 if (S[i+1] == '='):
#                     i += 2
#                 else:
#                     i += 1
#             else:
#                 i += 1
#             count += 1            
# else:
#     count += 1
# print(count)           
S = [x for x in str(input())]
i = 0
count = 0
strr = ['a','b','c','d','e','f','g','h','i','j','k','l' \
       ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
if len(S) >= 2:
    while True:
        if i > len(S)-1:
            break
        elif i == len(S)-1:
            if (S[i] in strr):
            #!= '-') and (S[i] != '='):
                count += 1                            
            break
        elif (i == len(S)-3) and (S[i:i+3]=='dz='):
            count +=1
            break
        else:
            print(i,S[i])
            if S[i] == 'c':
                if (S[i+1] == '=') or (S[i+1] == '-'):
                    i += 2
                else:
                    i += 1
            elif S[i] == 'd':
                if (S[i+1:i+3] == 'z='):
                    i += 3
                elif (S[i+1] == '-'):
                    i += 2
                else:
                    i += 1
            elif (S[i] == 'l') or (S[i]=='n'):
                if (S[i+1] == 'j'):
                    i += 2
                else:
                    i += 1
            elif (S[i] == 's') or (S[i]=='z'):
                if (S[i+1] == '='):
                    i += 2
                else:
                    i += 1
            else:
                i += 1
            count += 1            
else:
    count += 1
print(count)