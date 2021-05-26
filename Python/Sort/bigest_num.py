"""
https://programmers.co.kr/learn/courses/30/parts/12198
PROGRAMMERS SORT BIGEST NUMBER
"""

def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda x:x*3, reverse=True)
    
    answer = "".join(str_numbers)

    # [0,0,0]일 때 '000'이 아니라 "0"
    if answer[0] == "0": answer="0"
    
    return answer

def main():
    numbers1 = [6, 10, 2]
    numbers2 = [3, 30, 34, 5, 9]
    numbers3 = [10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers4 = [0, 0, 0, 0]
    numbers5 = [21, 212]
    numbers6 = [40, 403]

    result1 = "6210"
    result2 = "9534330"
    result3 = "987654321101000"
    result4 = "0"
    result5 = "21221"
    result6 = "40403"

    if solution(numbers1) == result1: print("RIGHT1")
    if solution(numbers2) == result2: print("RIGHT2")
    if solution(numbers3) == result3: print("RIGHT3")
    if solution(numbers4) == result4: print("RIGHT4")
    if solution(numbers5) == result5: print("RIGHT5")
    if solution(numbers6) == result6: print("RIGHT6")

if __name__=="__main__":
    main()

'''
# 원래 내가 썼던 코드
# 모든 테스트케이스, 예외상황을 통과하는데 히든테케 1, 2, 3, 5, 6 번에서 시간 초과가 뜬다.
# 이 이상 줄일 방법을 모르겠어서 구글링해서 각 숫자의 자릿수를 1000 이하의 단위로 맞춰주면 이중 for문을 쓰지 않고 정렬 한번으로 된다는 것을 알게 되었다.

def solution(numbers):
    # 첫 번째 자리수가 큰 순서대로 정렬하기 위해서 int->string으로 변환
    str_numbers = []
    for i in numbers:
        str_numbers.append(str(i))
    
    # 첫 번째 자리수가 큰 순서대로 정렬
    str_numbers.sort(reverse=True)
        
    # 여러 반례의 경우 정렬
    for i in range(len(str_numbers)-1, 0, -1):
        for j in range(i):
            if str_numbers[j][0] == str_numbers[j+1][0]:
                if str_numbers[j] + str_numbers[j+1] < str_numbers[j+1]+str_numbers[j]:
                    str_numbers[j], str_numbers[j+1] = str_numbers[j+1], str_numbers[j]
    
    answer = "".join(str_numbers)

    # [0,0,0]일 때 '000'이 아니라 "0"
    if answer[0] == "0": answer="0"
    
    return answer
'''

'''
# 다른사람이 쓴 매우 간결한 코드

def solution(num):
    num = list(map(str, num)) 
    num.sort(key = lambda x : x*3, reverse = True) 
    return str(int(''.join(num)))

lambda x : x*3은 num 인자 각각의 문자열을 3번 반복한다는 뜻이다. 
x*3을 하는 이유? -> num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 뜻.
ex) 403 40 4 -> 403403403 404040 444 로 바꾼뒤
첫 번째 자리: 4 4 4 모두 같음
두 번째 자리: 0 0 4 로 444가 제일 큼
세 번째 자리: 3 4 x 로 404040이 다음으로 큼
=> 조합했을 때 큰 순서: 4 40 403 이 된다.

'''

'''
# 다른사람이 쓴 매우 간결한 코드2
# 순열 조합 함수인 permutations를 사용했지만, 모든 경우의 수를 구하고 그 중 가장 큰 경우의 수를 구하는 것이기 때문에 이것도 시간 초과가 뜬다.

from itertools import permutations 
def solution(num): 
    permute = list(permutations(num,len(num))) 
    list_permute = [''.join(map(str,i)) for i in permute] 
    answer = max(list_permute) 
    return answer

'''