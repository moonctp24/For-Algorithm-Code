'''
정수가 저장된 배열 nums이 주어졌을 때, nums의 원소중 두 숫자를 더해서
target이 될 수 있으면 True, 불가능하면 False를 반환하세요.
같은 원소를 두 번 사용할 수 없습니다.

제약조건
2 <= nums.length <= 10^4
'''

# two pointer used
def twoSum(nums, target):
    nums.sort() # O(n log n)
    n = len(nums)
    
    i1 = 0
    i2 = n-1
    
    # O(n)
    while i2>i1:
        if nums[i1] + nums[i2] == target:
            return True
        elif nums[i1] + nums[i2] < target:
            i1 += 1
        elif nums[i1] + nums[i2] > target:
            i2 -= 1
    return False

print(twoSum(nums=[2, 1, 5, 7], target=4))
print(twoSum(nums=[4, 1, 9, 7, 5, 3, 16], target=14))
print(twoSum(nums=[4, 1, 9, 7, 5, 3, 16], target=15))