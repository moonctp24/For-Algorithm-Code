"""
SSG.COM 코딩테스트
Prob2. 부정행위자 찾기
"""

'''푼 번호를 추출하는 함수'''
from cv2 import sort


def solvNumList (num, solvlist):
    tmpList = []
    for i in solvlist:
        if num == i[0]:
            tmpList.append(i[1])
    tmpList.sort()
    
    return tmpList

'''푼 번호의 점수를 추출하는 함수'''
def solvScoreList (num, num2, solvlist):
    solvlist = sorted(solvlist, key=lambda x: (x[0], x[1]))
    tmpList = []
    for i in solvlist:
        if num == i[0]:
            for j in solvlist:
                if num2 == j[0] and i[1] == j[1]:
                    tmpList.append(i[2])
    return tmpList

def solution(logs):
    '''1. 데이터 정제'''
    arry2d = []
    for i in logs:
        arry2d.append(i.split())
    
    for i in arry2d:
        i[1] = int(i[1])
    
    logs2 = []
    for i in range(len(arry2d)):
        logs2.append(arry2d[i])
        
        for j in range(i+1, len(arry2d)):
            if int(arry2d[i][0]) == int(arry2d[j][0]) and int(arry2d[i][1]) == int(arry2d[j][1]) and int(arry2d[i][2]) != int(arry2d[j][2]):
                logs2.pop()
    
    '''2. student: 각 시험자가 푼 문제 수 count'''
    student = {}
    
    for i in logs2:
        if i[0] in student:
            student[i[0]] = student[i[0]] + 1
        else:
            student[i[0]] = 1
    
    '''3. 부정행위자 검증'''
    answer = []
    for k in student:
        for k2 in student:
            # count < 5 이면 넣지 않음
            if student.get(k) < 5:
                continue
            else:
                if student[k] == student[k2] and k != k2: # 다른 두 학생이 푼 문제수가 같다
                    if solvNumList(k, logs2) == solvNumList(k2, logs2): # 푼 문제의 번호 같다
                        if solvScoreList(k, k2, logs2) == solvScoreList(k2, k, logs2): # 푼 문제의 점수 같다
                            answer.append(k)
                            answer.append(k2)

    tmpset = set(answer)
    answer = list(tmpset)
    answer.sort()
    
    '''4. 부정행위 없으면 None 출력'''
    if len(answer) == 0:
        answer.append("None");
    
    return answer

def main():
    logs1 = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]
    #logs2 = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]
    logs3 = ["1901 10 50", "1909 10 50"]
    logs4 = ["0001 1 0", "0001 2 0", "0001 3 0", "0001 4 0", "0001 5 0", "0456 1 0", "0456 2 0", "0456 3 0", "0456 3 0", "0456 4 0", "0456 5 0"]
    
    result1 = ["0001", "0002"]
    result2 = ["1101", "1102", "1901", "1902", "1903"]
    result3 = ["None"]
    result4 = ["0001", "0456"]

    if solution(logs1) == result1: print("RIGHT1")
    #if solution(logs2) == result2: print("RIGHT2")
    if solution(logs3) == result3: print("RIGHT3")
    if solution(logs4) == result4: print("RIGHT4")

if __name__=="__main__":
    main()