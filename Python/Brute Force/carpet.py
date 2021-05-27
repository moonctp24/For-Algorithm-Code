"""
https://programmers.co.kr/learn/courses/30/parts/12230
PROGRAMMERS BRUTE FORCE CARPET
"""

def solution(brown, yellow):
    width = 0
    height = 0
    
    for i in range(1, yellow+1):
        if yellow%i == 0:
            if (yellow/i + 2) * (i + 2) - yellow == brown:
                width = yellow/i + 2
                height = i + 2
                break
    
    answer = [width, height]
    return answer

def main():
    brown1 = 10
    brown2 = 8
    brown3 = 24
    
    yellow1 = 2
    yellow2 = 1
    yellow3 = 24

    result1 = [4, 3]
    result2 = [3, 3]
    result3 = [8, 6]

    if solution(brown1, yellow1) == result1: print("RIGHT1")
    if solution(brown2, yellow2) == result2: print("RIGHT2")
    if solution(brown3, yellow3) == result3: print("RIGHT3")

if __name__=="__main__":
    main()