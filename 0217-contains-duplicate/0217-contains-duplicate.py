class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for a in range(len(nums)-1):
            if nums[a]==nums[a+1]:
                return True
        else:
             return False