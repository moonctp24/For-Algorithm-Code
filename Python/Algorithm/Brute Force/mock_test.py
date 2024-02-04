"""
https://programmers.co.kr/learn/courses/30/parts/12230
PROGRAMMERS BRUTE FORCE MOCK TEST
"""

def solution(answers):
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    count = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == stu1[i%5]: count[0]+=1
        if answers[i] == stu2[i%8]: count[1]+=1
        if answers[i] == stu3[i%10]: count[2]+=1
    
    answer = []
    for i in range(len(count)):
        if max(count) == count[i]:
            answer.append(i+1)
            
    answer.sort()
    return answer

def main():
    answers1 = [1, 2, 3, 4, 5]
    answers2 = [1, 3, 2, 4, 2]

    result1 = [1]
    result2 = [1, 2, 3]

    if solution(answers1) == result1: print("RIGHT1")
    if solution(answers2) == result2: print("RIGHT2")

if __name__=="__main__":
    main()