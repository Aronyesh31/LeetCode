class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold, sold, rest = float("-inf"), 0, 0
        for p in prices:
            hold, sold, rest = max(hold, rest - p), hold + p, max(rest, sold)
        return max(sold, rest)
