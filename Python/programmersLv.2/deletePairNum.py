"""
https://school.programmers.co.kr/learn/courses/30/lessons/12973
PROGRAMMERS 짝지어 제거하기
"""

def solution(s):
    stck = []
    for c in s: # O(n)
        if len(stck) == 0:
            stck.append(c)
        else:
            if c == stck[-1]:
                stck.pop()
                continue
            else:
                stck.append(c)
    if len(stck) == 0:
        return 1
    else:
        return 0

s1 = "baabaa"
s2 = "cdcd"

result1 = 1
result2 = 0

if solution(s1) == result1: print("RIGHT1")
if solution(s2) == result2: print("RIGHT2")