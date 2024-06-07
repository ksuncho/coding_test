card = []
gp = 0
n = 0

def trans(grade):
    x = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
    return x.get(grade,0)

for i in range(2):
    card.append(list(map(str, input().split())))
for i in range(2):
    if card[i][2] != 'P':
        gp += float(card[i][1])*float(trans(card[i][2]))
        n += float(card[i][1])
    
print(gp/n)