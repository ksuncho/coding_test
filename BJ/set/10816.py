import sys
N= int(sys.stdin.readline().rstrip())
cards = [int(x) for x in sys.stdin.readline().split()]
card_dict = {}
for i in cards:
    card_dict[i] = card_dict.get(i,0) + 1
M= int(sys.stdin.readline().rstrip())
for i in map(int, sys.stdin.readline().split()):
    print(card_dict.get(i,0),end=' ')
