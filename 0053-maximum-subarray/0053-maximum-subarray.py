class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = cur = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best
