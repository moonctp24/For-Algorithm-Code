"""
BAEKJOON 1085번 직사각형에서 탈출
https://www.acmicpc.net/problem/1085
"""

x, y, w, h = (map(int, input().split()))
print(min(w-x, x-0, h-y, y-0))

# 오늘 신한 코테쳤는데, 문제 유출 금지라네요..ㅎ 대신 간단한 알고리즘코드 올립니당