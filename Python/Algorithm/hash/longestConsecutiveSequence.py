'''
정렬되어 있지 않은 정수형 배열 nums가 주어졌다. nums 원소를 가지고 만들 수 있는 가장 긴 연속된 수의 갯수는 몇개인지 반환

제약조건
0 <= nums.length <= 10^5
'''

# sort used
def LongestConsecutiveSequence(nums):
    if len(nums) <= 1:
        return len(nums)
    
    nums.sort() # O(n log n)
    
    nowN = nums[0]
    count = 1
    cList = []
    init = True
    for n in nums: # O(n)
        if init:
            nowN = n
            init = False
            continue
        else:
            if n == nowN:
                continue
            if n == nowN +1:
                count += 1
                nowN += 1
            else:
                init = True
                cList.append(count)
                count = 1
    cList.append(count)
    return(max(cList)) # O(n)

print(LongestConsecutiveSequence(nums=[100, 4, 200, 1, 3, 2]))
print(LongestConsecutiveSequence(nums=[0,3,7,2,5,8,4,6,0,1]))
print(LongestConsecutiveSequence(nums=[3,1,5,9,7,11]))
print(LongestConsecutiveSequence(nums=[]))
print(LongestConsecutiveSequence(nums=[11]))
