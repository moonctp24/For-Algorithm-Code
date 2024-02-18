'''
정수가 저장된 배열 nums이 주어졌을 때, nums의 원소중 두 숫자를 더해서
target이 될 수 있으면 True, 불가능하면 False를 반환하세요.
같은 원소를 두 번 사용할 수 없습니다.

제약조건
2 <= nums.length <= 10^4
'''

# Dictionary used
def twoSum(nums, target):
    # numDic = {}
    # for n in nums:
    #     numDic[target-n] = n
    # for k,v in numDic.items():
    #     if v in numDic:
    #         if v == numDic[v]:
    #             continue
    #         else:
    #             return True
    # return False
    numDic = {}
    
    # O(n)
    for n in nums:
        numDic[n] = 1
    
    # O(n)
    for d in numDic:
        if target-d in numDic:
            if d == target-d:
                continue
            else:
                return True
    return False

print(twoSum(nums=[2, 1, 5, 7], target=4))
print(twoSum(nums=[4, 1, 9, 7, 5, 3, 16], target=14))
print(twoSum(nums=[4, 1, 9, 7, 5, 3, 16], target=15))