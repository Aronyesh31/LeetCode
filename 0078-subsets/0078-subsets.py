class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        for x in nums:
            res += [s + [x] for s in res]
        return res
