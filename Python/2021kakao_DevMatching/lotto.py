"""
https://programmers.co.kr/learn/challenges
PROGRAMMERS 2021 KAKAO DEV-MATCHING LOTTOS
"""

def solution(lottos, win_nums):
    count = 0
    count0 = 0
    for i in lottos:
        if i == 0: count0+=1
        for j in win_nums: 
            if i == j: count+=1
    
    answer = []
    # hiest rank
    highest = count+count0
    if highest < 2: answer.append(6)
    else: answer.append(6-highest+1)

    # lowest rank
    if count < 2: answer.append(6)
    else: answer.append(6-count+1)
    
    return answer

def main():
    lottos1 = [44, 1, 0, 0, 31, 25]
    lottos2 = [0, 0, 0, 0, 0, 0]
    lottos3 = [45, 4, 35, 20, 3, 9]

    win_nums1 = [31, 10, 45, 1, 6, 19]
    win_nums2 = [38, 19, 20, 40, 15, 25]
    win_nums3 = [20, 9, 3, 45, 4, 35]

    result1 = [3, 5]
    result2 = [1, 6]
    result3 = [1, 1]

    if solution(lottos1, win_nums1) == result1: print("RIGHT1")
    if solution(lottos2, win_nums2) == result2: print("RIGHT2")
    if solution(lottos3, win_nums3) == result3: print("RIGHT3")

if __name__=="__main__":
    main()