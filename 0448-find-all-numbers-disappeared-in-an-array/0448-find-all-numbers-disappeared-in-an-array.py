class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for x in nums:
            i = abs(x) - 1
            nums[i] = -abs(nums[i])
        return [i + 1 for i, x in enumerate(nums) if x > 0]
