# hidden tc까지 다 맞음

import math

def time_calculation(end, start):
    end = list(map(int, end.split(':')))
    start = list(map(int, start.split(':')))
    
    if start[1] > end[1]:
        answer = (end[0]-start[0]-1)*60 + (end[1]-start[1]+60)
    else:
        answer = (end[0]-start[0])*60 +(end[1]-start[1])
    return answer

def not_out(start):
    start = list(map(int, start.split(':')))
    answer = (23-start[0])*60 + (59-start[1])
    return answer

def solution(fees, records):
    records2 = []
    for i in records:
        records2.append(i.split())

    car_list = []
    car_dic = {}
    during_dic = {}
    for a, b, c in records2:
        if c == "IN":
            during_dic[b] = 0
    for a, b, c in records2:
        if c == "IN":
            car_dic[b] = a
            car_list.append(b)
        if c == "OUT":
            # during_dic.update(b:time_calculation(a, car_dic[b]))
            during_dic[b] += time_calculation(a, car_dic[b])
            del car_list[car_list.index(b)]

    while True:
        if len(car_list) == 0:
            break
        else:
            during_dic[car_list[0]] += not_out(car_dic[car_list[0]])
            del car_list[0]

    fee_dic = during_dic.copy()

    for a, b in during_dic.items():
        if b <= fees[0]:
            fee_dic[a] = fees[1]
        else:
            fee_dic[a] = math.ceil((fee_dic[a]-fees[0])/fees[2]) * fees[3] + fees[1]

    sorted_fee = sorted(fee_dic.items())

    answer = []
    for i in sorted_fee:
        answer.append(i[1])

    return answer

def main():
    fees1 = [180, 5000, 10, 600]
    fees2 = [120, 0, 60, 591]
    fees3 = [1, 461, 1, 10]

    records1 = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    records2 = ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]
    records3 = ["00:00 1234 IN"]

    result1 = [14600, 34400, 5000]
    result2 = [0, 591]
    result3 = [14841]


    if(solution(fees1, records1) == result1): print("RIGHT1")
    else: print('TRY AGAIN')
    if(solution(fees2, records2) == result2): print("RIGHT1")
    else: print('TRY AGAIN')
    if(solution(fees3, records3) == result3): print("RIGHT1")
    else: print('TRY AGAIN')


if __name__ == "__main__":
    main()
