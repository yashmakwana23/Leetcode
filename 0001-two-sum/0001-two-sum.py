class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, a in enumerate(nums):
            item = target - a
            if item in hash_map:
                return [hash_map[item], i]
            
            hash_map[a] = i