"""
https://programmers.co.kr/learn/courses/30/parts/12198
PROGRAMMERS SORT H INDEX
"""

def solution(citations):
    answer = 0

    citations.sort()
    count = 0
    for i in range(len(citations)-1, -1, -1):
        if i+1 <= citations[len(citations)-1-i]: count+=1
            
    return count

def main():
    citations1 = [3, 0, 6, 1, 5]
    citations2 = [0, 2, 5, 6, 8, 9, 10]
    citations3 = [5, 5, 5, 5, 5]
    citations4 = [5, 5, 5, 5]
    citations5 = [31, 66]

    result1 = 3
    result2 = 5
    result3 = 5
    result4 = 4
    result5 = 2

    if solution(citations1) == result1: print("RIGHT1")
    if solution(citations2) == result2: print("RIGHT2")
    if solution(citations3) == result3: print("RIGHT3")
    if solution(citations4) == result4: print("RIGHT4")
    if solution(citations5) == result5: print("RIGHT5")

if __name__=="__main__":
    main()
    