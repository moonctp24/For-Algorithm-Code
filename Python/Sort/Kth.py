"""
https://programmers.co.kr/learn/courses/30/parts/12198
PROGRAMMERS SORT Kth NUMBER
"""

def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        slice_array = array[commands[i][0]-1:commands[i][1]]
        slice_array.sort()
        answer.append(slice_array[commands[i][2]-1])
    return answer

def main():
    array1 = [1, 5, 2, 6, 3, 7, 4]
    commands1 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    result1 = [5, 6, 3]

    if(solution(array1, commands1) == result1): print("RIGHT")

if __name__=="__main__":
    main()

'''
# 다른사람이 쓴 매우 간결한 코드
# map 함수를 사용하여 한 줄에 끝냄
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''