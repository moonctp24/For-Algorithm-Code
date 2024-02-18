"""
https://school.programmers.co.kr/learn/courses/30/lessons/70129
PROGRAMMERS 이진 변환 반복하기
"""

def solution(s):
    nextS = s
    dlt0Cnt = 0
    ttlCnt = 0
    while nextS != '1':
        newS = ''
        # delete 0
        for c in nextS:
            if c == '0':
                dlt0Cnt += 1
                continue
            else:
                newS += c
        
        # to binary number
        newN = len(newS)
        newS = ''
        while newN > 1:
            m, n= divmod(newN, 2)
            newN = m
            newS += str(n)
        newS += '1'
        nextS = ''
        for c in range(len(newS)-1, -1, -1):
            nextS += newS[c]
        ttlCnt += 1
    answer = [ttlCnt, dlt0Cnt]
    return answer

def main():
    s1 = "110010101001"
    s2 = "01110"
    s3 = "1111111"

    result1 = [3,8]
    result2 = [3,3]
    result3 = [4,1]

    if solution(s1) == result1: print("RIGHT1")
    if solution(s2) == result2: print("RIGHT2")
    if solution(s3) == result3: print("RIGHT3")

if __name__=="__main__":
    main()
