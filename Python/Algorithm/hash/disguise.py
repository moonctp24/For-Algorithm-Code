"""
https://programmers.co.kr/learn/courses/30/parts/12077
PROGRAMMERS HASH Disguise
"""

# 코드가 너무 복잡해져서 다른 사람의 로직 찾아봤음
# 경우의 수 문제로 생각하면 훨씬 간단해지는데, 왜 그 생각을 못했을까..
def solution(clothes):
    answer = 1

    clothes_type = {}
    for i in range(len(clothes)):
        if clothes[i][1] in clothes_type:
            clothes_type[clothes[i][1]] += 1
        else: clothes_type[clothes[i][1]] = 1
        
    for i in clothes_type.values():
        answer *= i+1

    return answer-1

def main():
    clothes1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    clothes2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    clothes3 = [["round_glasses", "eyewear"], ["black_sunglasses", "eyewear"], ["blue_shirts", "top"], ["jean", "bottom"]]

    result1 = 5
    result2 = 3
    result3 = 11

    if(solution(clothes1) == result1): print("RIGHT1")
    if(solution(clothes2) == result2): print("RIGHT2")
    if(solution(clothes3) == result3): print("RIGHT3")

if __name__ == "__main__":
    main()
    

'''
key. (종류별갯수+1)를 전부 곱하면 모든 종류의 옷을 고르거나 고르지 않는 경우의 수가 된다. 여기서 모든 옷을 고르지 않는 한 가지의 경우의 수를 -1 해주기
1. 의상 종류별 갯수 구함
2. 종류별갯수+1 전부 곱하기
3. 모든 옷을 고르지 않는 한 가지 -1
'''

'''
# 다른사람이 쓴 매우 간결한 코드
# counter 클래스, reduce 사용해서 계산을 한번에 함
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
'''