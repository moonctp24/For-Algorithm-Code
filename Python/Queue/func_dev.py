'''
https://programmers.co.kr/learn/courses/30/parts/12081
PROGRAMMERS STACK/QUEUE FUNCTION DEVELOP
'''

import math

def solution(progresses, speeds):
    rest = []

    for i, j in zip(progresses, speeds):
        rest.append(math.ceil((100-i)/j))
        
    answer = []
    num = []
    for i in range(len(rest)):
        num.append(rest[i])
        if i+1 <= len(rest)-1 and num[0] >= rest[i+1]: continue
        else:
            answer.append(len(num))
            num.clear()
    
    return answer

def main():
    progresses1 = [93, 30, 55]
    progresses2 = [95, 90, 99, 99, 80, 99]

    speeds1 = [1, 30, 5]
    speeds2 = [1, 1, 1, 1, 1, 1]

    result1 = [2, 1]
    result2 = [1, 3, 2]

    if solution(progresses1, speeds1) == result1: print("RIGHT1")
    if solution(progresses2, speeds2) == result2: print("RIGHT2")

if __name__=="__main__":
    main()