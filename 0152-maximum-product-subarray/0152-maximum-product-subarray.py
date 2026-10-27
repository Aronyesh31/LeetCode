class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        best = hi = lo = nums[0]
        for x in nums[1:]:
            hi, lo = max(x, hi * x, lo * x), min(x, hi * x, lo * x)
            best = max(best, hi)
        return best
