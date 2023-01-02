class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list3=set()
        for a in range(len(nums1)):
            for b in range(len(nums2)):
                if nums1[a]==nums2[b]:
                    list3.add(nums1[a])
        return list3