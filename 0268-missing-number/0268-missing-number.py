class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        Asum=sum(nums)
        n=len(nums)
        Bsum=(n * ( n + 1)) / 2
        return int (Bsum-Asum)