class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        best = cur = 0
        for x in nums:
            cur = cur + 1 if x else 0
            best = max(best, cur)
        return best
