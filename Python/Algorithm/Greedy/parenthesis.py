"""
BAEKJOON 1541번 잃어버린 괄호
https://www.acmicpc.net/problem/1541
"""

# - 부터 다음 -까지 괄호

str = input()

expre = []
until_minus = []
tmp = ['0']
toggle = False
for i in range(len(str)):
    if str[i] == '+' and toggle == False:
        until_minus.append(int(tmp[0]))
        tmp = ['']
    elif str[i] == '+' and toggle == True:
        expre.append(int(tmp[0]))
        tmp = ['']
    elif str[i] == '-':
        expre.append(int(tmp[0]))
        tmp = ['']
        toggle = True
    else :
        tmp[0] += str[i]
    
    if i == len(str)-1:
        expre.append(int(tmp[0]))

result = 0
for i in until_minus:
    result += i

result += expre[0]
for i in expre[1:]:
    result -= i

print(result)

# 구글링해서 다른 사람 답안을 봤는데 대부분 이중for문을 썼다.
# 나는 단일for문을 썼는데, 돌려보니 둘 다 29200KB, 64ms 똑같이 걸렸다.