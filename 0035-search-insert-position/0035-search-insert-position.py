class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<nums[0]:
            return 0
        for i in range(len(nums)):
            try:
                if target==nums[i]:
                    return i
                elif target<nums[i+1]:
                    return i+1
            except IndexError:
                pass
        return (len(nums))