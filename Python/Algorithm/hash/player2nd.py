def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    
    return participant[len(participant)-1]

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