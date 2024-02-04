"""
BAEKJOON 1339번 단어 수학
https://www.acmicpc.net/problem/1339
"""


N = int(input())
wordsList = [] # 입력받은 단어 List
charNumDic = {} # 숫자를 배정받은 문자
remainMaxNum = 9 # 배정할 수 있는 숫자 중 최댓값

for i in range(N):
    wordsList.append(input())

for i in wordsList:
    for j in range(len(i)):
        # print(i[j])
        if i[j] in charNumDic:
            charNumDic[i[j]] += 10**(len(i)-j-1)
        else:
            charNumDic[i[j]] = 10**(len(i)-j-1)

# 단어를 가중치 순서로 정렬
charNumDic = sorted(charNumDic.items(), key=lambda x: x[1], reverse=True)

newCharNumDic = {}
for i in charNumDic:
    # print(i[0])
    newCharNumDic[i[0]] = remainMaxNum
    remainMaxNum -= 1

# 다 더하기
result = 0
for i in wordsList:
    for j in range(len(i)):
        result += newCharNumDic[i[j]] *(10**(len(i)-j-1))

print(result)
'''
<첫번째 시도>
1. 길이가 더 긴 단어를 선택해서 9, 8, 7, ... 순서로 넣는다.
2. 남은 단어의 길이가 같아지면 OR 처음부터 같은 길이의 단어가 여러개 들어왔다면
   975...
   864...
   이렇게 나눠서 배정한다.
3. 반복문을 돌때마다 이미 숫자가 배정된 문자가 나오면 그대로 넣고, 다음 인덱스로 넘어간다
* 반복문의 인덱스 => 0 ~ maxLen
    i=0 -> 'a'bcde
    
    i=1 -> a'b'cde
            'f'ghi

    i=2 -> ab'c'de
            f'g'hi
             'j'kl
    
    i=3 -> abc'd'e
            fg'h'i (index = len(fghi) - len(abcde) + i)
             j'k'l (index = len(jki)  - len(abcde) + i)
              'm'n (index = len(mn)   - len(abcde) + i)
              사이사이에 if charNow in charNumDic: continue

=> 위 알고리즘의 예외상황
EX) AAA + BB + BB + BB + BB + BB + BB + BB + BB + BB + BB + BB
일 때, 위 알고리즘대로라면

AAA = 999
BB = 88
이므로 999 + 88 + 88 + 88 + 88 + 88 + 88 + 88 + 88 + 88 = 1967

하지만 BB의 갯수가 많기 때문에 B에 9를 할당해줄 때 더 높은 수가 나오게 된다.
888 + 99 + 99 + 99 + 99 + 99 + 99 + 99 + 99 + 99 = 1977
'''

'''
<두번째 시도>
1. 길이 뿐 아니라, 그 알파벳이 사용된 위치에 가중치?를 두고 정렬한 후 9,8,7,...은 나중에 대입해준다.

예를들어 입력값 ABC, BCD
각 숫자에 1을 대입한다고 할 때, 각 숫자가 만들 수 있는 값은 다음과 같다.

A : 100
B : 10 + 100 = 110
C : 1 + 10 = 11
D : 1

따라서, B가 가장 큰 결과를 만들고
차례대로 A, C, D가 그 뒤를 잇게 된다.
그래서 8, 9, 7, 6의 순서로 대입하면 가장 큰 숫자를 만들 수 있게 된다.(답 : 1873)

즉, 모든 단어의 알파벳을 통해 그 자리수를 곱하여 해당 숫자를 모두 더할 시 만들 수 있는 가장 큰 값을 계산하여 정렬한 뒤 9부터 차례대로 숫자를 대입하고 그 결과를 출력
'''