class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        reach = 1
        for x in nums:
            reach |= reach << x
        return bool(reach >> (total // 2) & 1)
