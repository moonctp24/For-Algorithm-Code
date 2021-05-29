'''
https://programmers.co.kr/learn/courses/30/parts/12081
PROGRAMMERS STACK/QUEUE TRUCK CROSSING THE BRIDGE
'''

def solution(bridge_length, weight, truck_weights):
    q1 = []
    q2 = []
    rest = []
    total_num = len(truck_weights)
    sec = 0
    while True:
        # terminal condition
        if len(q1) == total_num: break
        sec +=1

        if len(truck_weights) > 0 and (sum(q2) + truck_weights[0]) <= weight:
            q2.append(truck_weights[0])
            rest.append(0)
            truck_weights.pop(0)
        for j in range(len(rest)): rest[j]+=1
        if rest[0] >= bridge_length:
            q1.append(q2[0])
            q2.pop(0)
            rest.pop(0)

    return sec+1

def main():
    bridge_length1 = 2
    bridge_length2 = 100
    bridge_length3 = 100

    weight1 = 10
    weight2 = 100
    weight3 = 100

    truck_weights1 = [7, 4, 5, 6]
    truck_weights2 = [10]
    truck_weights3 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

    result1 = 8
    result2 = 101
    result3 = 110

    if solution(bridge_length1, weight1, truck_weights1) == result1: print("RIGHT1")
    if solution(bridge_length2, weight2, truck_weights2) == result2: print("RIGHT2")
    if solution(bridge_length3, weight3, truck_weights3) == result3: print("RIGHT3")
    
if __name__=="__main__":
    main()