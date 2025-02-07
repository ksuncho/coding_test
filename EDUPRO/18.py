import sys
if sys.platform == 'win32':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/18.txt')

input = sys.stdin.readline
from collections import defaultdict

devlist = defaultdict(list)

def register(pid, salary, C, J, P):
    devlist[pid]=[salary,C,J,P]

def cancel(pid):
    devlist[pid].clear()

def update(pid,flag,X):
    devlist[pid][flag+1]=X