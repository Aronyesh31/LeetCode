class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(i):
            if i == len(nums):
                res.append(nums[:])
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        dfs(0)
        return res
