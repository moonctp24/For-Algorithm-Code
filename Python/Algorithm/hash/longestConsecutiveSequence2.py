'''
정렬되어 있지 않은 정수형 배열 nums가 주어졌다. nums 원소를 가지고 만들 수 있는 가장 긴 연속된 수의 갯수는 몇개인지 반환

제약조건
0 <= nums.length <= 10^5
'''

# Dictionary used
def LongestConsecutiveSequence(nums):
    if len(nums) <= 1:
        return len(nums)
    
    nDic = {}
    for n in nums: # O(n)
        nDic[n] = 1
    
    cnt = 1
    cList = []
    for d in nDic: # O(n)
        if d-1 in nDic:
            continue
        else:
            cnt = 1
            while d+1 in nDic:
                cnt +=1
                d += 1
            cList.append(cnt)
    return(max(cList)) # O(n)

print(LongestConsecutiveSequence(nums=[100, 4, 200, 1, 3, 2]))
print(LongestConsecutiveSequence(nums=[0,3,7,2,5,8,4,6,0,1]))
print(LongestConsecutiveSequence(nums=[3,1,5,9,7,11]))
print(LongestConsecutiveSequence(nums=[]))
print(LongestConsecutiveSequence(nums=[11]))
