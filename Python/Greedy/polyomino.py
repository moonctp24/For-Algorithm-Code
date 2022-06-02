"""
BAEKJOON 1343번 폴리오미노
https://www.acmicpc.net/problem/1343
"""

strOrigin = input()
strOrigin = strOrigin.replace('XXXX', 'AAAA')
strOrigin = strOrigin.replace('XX', 'BB')

if 'X' in strOrigin:
    print(-1)
else:
    print(strOrigin)
'''
str = list(filter(None, map(str, strOrigin.split('.'))))

strA = 'AAAA'
strB = 'BB'

result = 0
resultList = []
for i in str:
    if len(i) % 4 == 0:
        resultList.append(strA * (len(i) // 4))
    elif len(i) % 4 == 2:
        resultList.append(strA * (len(i) // 4) + strB)
    else:
        result = -1
        break
if len(resultList) == 0:
    result = -1

if result == -1:
    print(-1)
else:
    resultStr = ''
    a = 0
    prePoint = 1
    for i in strOrigin:
        # print(resultStr)
        if i == '.':
            prePoint = 1
            resultStr += '.'
            continue
        
        if prePoint == 1:
            prePoint = 0
            resultStr += resultList[a]
            a += 1
    print(resultStr)
'''