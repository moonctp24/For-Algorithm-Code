# hidden tc까지 다 맞음

def solution(id_list, report, k):
    report.sort()
    report = list(set(report))

    report2 = []
    for i in report:
        report2.append(i.split())

    report3 = {}
    for i in report2:
        report3[i[1]] = 0
    
    for i in report2:
        report3[i[1]] = report3[i[1]]+1
    
    forbidden_list = []
    for key,val in report3.items():
        if val >= k:
            forbidden_list.append(key)
    
    answer = []
    for i in id_list:
        answer.append(0)

    for i in report2:
        if i[1] in forbidden_list:
            answer[id_list.index(i[0])] += 1

    print(answer)
    return answer

def main():
    id_list1 = ["muzi", "frodo", "apeach", "neo"]
    id_list2 = ["con", "ryan"]

    report1 = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]

    k1 = 2
    k2 = 3

    result1 = [2, 1, 1, 0]
    result2 = [0, 0]


    if(solution(id_list1, report1, k1) == result1): print("RIGHT1")
    else: print('TRY AGAIN')
    if(solution(id_list2, report2, k2) == result2): print("RIGHT2")
    else: print('TRY AGAIN')


if __name__ == "__main__":
    main()
