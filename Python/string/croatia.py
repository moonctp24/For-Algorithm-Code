"""
BAEKJOON 2941번 크로아티아 알파벳
https://www.acmicpc.net/problem/2941
"""

def isCroatia(inputStr):
    if len(inputStr) >= 3:
        startIdx = len(inputStr)-3
        endIdx = len(inputStr)
        if inputStr[startIdx:endIdx] == 'dz=':
            return inputStr[:startIdx]
    if len(inputStr) >= 2:
        startIdx = len(inputStr)-2
        endIdx = len(inputStr)

        if inputStr[startIdx:endIdx] == 'c=' or inputStr[startIdx:endIdx] == 'c-' or inputStr[startIdx:endIdx] == 'd-' or inputStr[startIdx:endIdx] == 'lj' or inputStr[startIdx:endIdx] == 'nj' or inputStr[startIdx:endIdx] == 's=' or inputStr[startIdx:endIdx] == 'z=':
            return inputStr[:startIdx]
        else:
            return inputStr
    else:
        return inputStr

croatiaStr = input()
count = 0

"""1. 문자 하나하나를 큐(문자열)에 담는다."""
queueStr = ''
remainList = []
for i in croatiaStr:
    queueStr += i
    # print(i, queueStr, count)
    
    """2. 반복문 한번 돌때마다 큐에 있는 문자를 합한 문자열이 크로아티아 문자인지 확인한다."""
    if len(isCroatia(queueStr)) != len(queueStr):  # 2-1. 확인 후 크로아티아 문자라면 count +1 하고, 큐에서 삭제 후 다음반복으로
        count += 1
        remainList.append(isCroatia(queueStr))
        queueStr = ''

remainList.append(queueStr)
# 남은 문자 개수만큼 count 더해주기
for i in remainList:
    count += len(i)

"""3. count 출력"""
print(count)