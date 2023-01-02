class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=0
        z=len(nums)
        while a!=len(nums):

            if nums[a]==val:
                nums.pop(a)
                nums.append("")
                z-=1
            else:
                a+=1
        return(z)