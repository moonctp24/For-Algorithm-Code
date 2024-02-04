"""
BAEKJOON 11399번 ATM
https://www.acmicpc.net/problem/11399
"""

n = int(input())
human = list(map(int, input().split()))

human.sort()

sum = 0
for i in range(len(human)):
    for j in range(i+1):
        sum += human[j]
print(sum)

# C++은 2015KB, 0ms 썼는데 Python은 29200KB, 128ms 썼다.. 확실히 C++이 빠르고 효율이 좋네

"""
# atm 2nd

n = int(input())
human = list(map(int, input().split()))

human.sort()

sum = 0
for i in range(0, len(human)):
    for j in range(0, i+1):
        sum = sum + human[j]
print(sum)

"""