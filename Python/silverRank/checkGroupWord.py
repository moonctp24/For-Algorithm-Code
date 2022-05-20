"""
BAEKJOON 1316번 그룹 단어 체커
https://www.acmicpc.net/problem/1316
"""

'''해당 단어가 그룹단어인 지 아닌 지 검증하는 함수'''
def isGroupWord(word):
    # 1. 단어 안에 각 그룹 알파벳 추출
    alphList = [word[0]]

    tmp = word[0]
    
    for i in range(len(word)):
        if tmp == word[i]:
            continue
        else:
            tmp = word[i]
            alphList.append(word[i])

    # 2. 그룹 단어인 지 확인
    for i in range(len(alphList)):
        for j in range(i+1, len(alphList)):
            if alphList[i] == alphList[j]:
                return False
            else:
                continue
    return True


# N 입력 받기
wordCnt = int(input())

# N 개수만큼 단어 입력받기
wordList = []
for i in range(wordCnt):
    wordList.append(input())

# 그룹 단어 체크 로직
# isGroupWord(wordList[0])
result = 0
for i in wordList:
    if isGroupWord(i):
        result = result+1
    else:
        continue
print(result)