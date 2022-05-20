"""
SSG.COM 코딩테스트
Prob1. 트럭 최대 주행 시간 문제
"""


def solution(v, a, b):
    hour = 0
    
    while(1):
        maxv = max(v)
        minv = min(v)
        
        # 로직 수행 전, 운행이 가능한 상태인 지 검사
        if maxv < a or minv < b:
            return hour
        
        '''운행 시작'''
        hour = hour + 1
        
        isCalculated = False
        
        for i in range(len(v)):
            #선두 트럭 연료 감소
            if v[i] == maxv and isCalculated == False:
                v[i] = v[i] - a
                isCalculated = True
            
            # 후위 트럭 연료 감소
            else:
                v[i] = v[i] - b

def main():
    v1 = [4, 5, 5]
    v2 = [4, 4, 3]
    
    a1 = 2
    a2 = 2
    
    b1 = 1
    b2 = 1
    
    result1 = 3
    result2 = 2

    if solution(v1, a1, b1) == result1: print("RIGHT1")
    if solution(v2, a2, b2) == result2: print("RIGHT2")

if __name__=="__main__":
    main()