from collections import Counter


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        count = Counter(nums)
        res, path = [], []

        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for x in count:
                if count[x]:
                    count[x] -= 1
                    path.append(x)
                    dfs()
                    path.pop()
                    count[x] += 1

        dfs()
        return res
