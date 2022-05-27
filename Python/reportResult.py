'''
2022 KAKAO BLIND RECRUITMENT 신고 결과 받기
'''

def solution(id_list, report, k):
    # 시간을 줄여주는 중요한 코드
    report = set(report)
    
    '''1. report 2차원 배열로 바꿈'''
    report_2arry = []
    for i in report:
        report_2arry.append(i.split())
        
    '''2. report에서 인덱스 [i][1] 인 이름 count <- 여기서 인덱스 [i][0]가 겹치지 않게 '''
    # id_list 순서대로 count
    suspendedUser = []
    my_report_list = [] # 유저별로 자기가 신고한 유저 list만들기
    for i in id_list:
        count_tmp = 0
        user_tmp = []
        my_report_list_tmp = []
        
        for j in range(len(report_2arry)):
            if i == report_2arry[j][1]: # 신고한 이름이 이미 신고한 사람이 아닐 때
                count_tmp = count_tmp + 1
                user_tmp.append(report_2arry[j][0])
            
            if i == report_2arry[j][0] and report_2arry[j][1] not in my_report_list_tmp: # 내가 신고한 유저 list
                my_report_list_tmp.append(report_2arry[j][1])

        if count_tmp >= k:
            suspendedUser.append(1)
        else:
            suspendedUser.append(0)

        my_report_list.append(my_report_list_tmp)

    
    '''3. count값이 k값을 넘기면 id_list 순으로 메일 받는 갯수 count'''
    answer = []
    for i in range(len(id_list)):
        for j in my_report_list:
            if suspendedUser[i] == 0 and id_list[i] in j:
                j.remove(id_list[i])
        
    for i in my_report_list:
        answer.append(len(i))
    return answer


def main():
    id_list1 = ["muzi", "frodo", "apeach", "neo"]
    id_list2 = ["con", "ryan"]
    
    report1 = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
    
    k1 = 2
    k2 = 3
    
    return1 = [2, 1, 1, 0]
    return2 = [0, 0]

    if solution(id_list1, report1, k1) == return1: print("RIGHT1")
    if solution(id_list2, report2, k2) == return2: print("RIGHT2")

if __name__=="__main__":
    main()