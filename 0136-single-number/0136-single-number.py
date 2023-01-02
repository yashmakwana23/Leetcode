class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        z={}
        i=1
        for a in nums:
            if a in z:
                z[a]=z[a]+1
            else:
                z[a]=i
        # print(z.values()).index(1)
        return(list(z.keys())
            [list(z.values()).index(1)])