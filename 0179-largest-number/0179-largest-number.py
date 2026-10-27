from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        strs = sorted(map(str, nums), key=cmp_to_key(lambda a, b: (b + a > a + b) - (b + a < a + b)))
        return "".join(strs).lstrip("0") or "0"
