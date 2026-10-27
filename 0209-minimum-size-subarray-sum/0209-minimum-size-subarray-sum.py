class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = total = 0
        best = float("inf")
        for right, x in enumerate(nums):
            total += x
            while total >= target:
                best = min(best, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if best == float("inf") else best
