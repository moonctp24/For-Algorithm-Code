"""
https://programmers.co.kr/learn/courses/30/parts/12244
PROGRAMMERS GREEDY GYM SUIT
"""
def solution(n, lost, reserve):
    # 여벌을 가져온 학생이 도난 당한 경우 각 list에서 제외
    for i in reserve:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
    
    # 규칙에 따라 체육복 빌려주기
    i = 0
    while True:
        # terminal condition
        if i == len(lost): break

        if lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            lost.pop(i)
            continue
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost.pop(i)
            continue
        if lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            lost.pop(i)
            continue
        i += 1

    answer = n - len(lost)
    return answer

def main():
    n1 = 5
    n2 = 5
    n3 = 11
    n4 = 5
    n5 = 10
    
    lost1 = [2, 4]
    lost2 = [2, 4]
    lost3 = [2, 4, 6, 8]
    lost4 = [1, 2]
    lost5 = [3, 9, 10]
    
    reserve1 = [1, 3, 5]
    reserve2 = [3]
    reserve3 = [2, 5, 6, 7]
    reserve4 = [2, 3]
    reserve5 = [3, 8, 9]

    result1 = 5
    result2 = 4
    result3 = 11
    result4 = 4
    result5 = 9

    if solution(n1, lost1, reserve1) == result1: print("RIGHT1")
    if solution(n2, lost2, reserve2) == result2: print("RIGHT2")
    if solution(n3, lost3, reserve3) == result3: print("RIGHT3")
    if solution(n4, lost4, reserve4) == result4: print("RIGHT4")
    if solution(n5, lost5, reserve5) == result5: print("RIGHT5")

if __name__=="__main__":
    main()