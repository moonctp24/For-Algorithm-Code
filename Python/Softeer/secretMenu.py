"""
현대 Softeer 문제 Level2. 비밀 메뉴
"""

import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
rightList = list(map(int, input().split()))
userList = list(map(int, input().split()))

rightStr = ''
userStr = ''
for r in rightList:
    rightStr += str(r)
for u in userList:
    userStr += str(u)

if(rightStr in userStr):
    print('secret')
else:
    print('normal')

'''
tc1
3 10 5
1 4 5
3 3 1 2 4 1 4 5 1 4

tc2
3 4 5
1 2 3
1 2 3 4
'''