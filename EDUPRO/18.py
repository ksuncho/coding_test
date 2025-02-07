import sys
if sys.platform == 'win32':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/18.txt')

input = sys.stdin.readline