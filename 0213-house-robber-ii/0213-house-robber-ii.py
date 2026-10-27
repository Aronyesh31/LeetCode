class Solution:
    def rob(self, nums: list[int]) -> int:
        def line(arr):
            prev = cur = 0
            for x in arr:
                prev, cur = cur, max(cur, prev + x)
            return cur

        if len(nums) == 1:
            return nums[0]
        return max(line(nums[1:]), line(nums[:-1]))
