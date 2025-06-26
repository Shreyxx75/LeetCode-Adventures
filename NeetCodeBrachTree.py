#217. Contains Duplicate
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
'''

#242. Valid Anagram
'''

'''

#1. Two Sum
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return prevMap[diff], i
            prevMap[n] = i
        return
'''
