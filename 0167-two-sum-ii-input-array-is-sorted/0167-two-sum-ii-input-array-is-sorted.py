class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while(left < right):
            target_sum = nums[left] + nums[right]
            if(target == target_sum):
                break
            elif(target < target_sum):
                right = right - 1
            elif(target > target_sum):
                left = left + 1
        return [left + 1, right + 1]