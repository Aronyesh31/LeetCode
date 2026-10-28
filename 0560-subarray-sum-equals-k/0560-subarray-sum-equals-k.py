from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        total = count = 0
        for x in nums:
            total += x
            count += seen[total - k]
            seen[total] += 1
        return count
