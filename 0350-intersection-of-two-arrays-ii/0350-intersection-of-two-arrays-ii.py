from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())
