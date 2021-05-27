"""
https://programmers.co.kr/learn/courses/30/parts/12230
PROGRAMMERS BRUTE PRIME NUMBER SEARCH
"""

from itertools import permutations

def solution(numbers):
    num = list(numbers)
    
    com = []
    for i in range(1, len(num)+1):
        com.append(list(map(''.join, permutations(num, i))))
    
    com2 = []
    for i in com:
        for j in i:
            com2.append(int(j))
    
    com2 = list(set(com2))
    
    answer = 0
    for i in com2:
        for j in range(2, i+1):
            if i%j == 0:
                if i == j: answer += 1
                else: break
        
    return answer

def main():
    numbers1 = "17"
    numbers2 = "011"

    result1 = 3
    result2 = 2

    if solution(numbers1) == result1: print("RIGHT1")
    if solution(numbers2) == result2: print("RIGHT2")

if __name__=="__main__":
    main()