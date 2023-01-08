class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos=0
        neg=0
        for a in nums:
            if a==0:
                continue
            if a>0:pos+=1
            else:neg+=1
        return max(pos,neg) 
        