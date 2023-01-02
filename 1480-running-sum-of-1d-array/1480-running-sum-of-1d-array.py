class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        op=[]
        a=0
        for i in range(len(nums)):
            sums= nums[i]+a
            op.append(sums)
            a=sums
        return op