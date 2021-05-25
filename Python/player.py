"""
https://programmers.co.kr/learn/courses/30/parts/12077
PROGRAMMERS HASH The player who could not finish
"""

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        answer = participant[i+1]

    return answer

def main():
    participant1 = ["leo", "kiki", "eden"]
    completion1 = ["eden", "kiki"]
    result1 = "leo"

    participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion2 = ["josipa", "filipa", "marina", "nikola"]
    result2 = "vinko"

    participant3 = ["mislav", "stanko", "mislav", "ana"]
    completion3 = ["stanko", "ana", "mislav"]
    result3 = "mislav"

    if(solution(participant1, completion1) == result1): print("RIGHT")
    if(solution(participant2, completion2) == result2): print("RIGHT")
    if(solution(participant3, completion3) == result3): print("RIGHT")
    
if __name__ == "__main__":
	main()

'''
# 다른사람이 쓴 매우 간결한 코드
# collections의 Counter 클래스 사용
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''

'''
# 처음에 작성한 코드.
# 히든 케이스는 전부 맞췄는데 효율성 테스트에서 전부 시간초과가 떠서
#  이중for문을 쓰면 안된다는 것을 깨닫고 정렬 후 for문을 한 번만 쓰는 코드로 작성
def solution(participant, completion):
    for i in range(len(completion)):
        for j in range(len(participant)):
            if completion[i] == participant[j]:
                del participant[j]
                break
    
    answer = participant[0]
    return answer
'''