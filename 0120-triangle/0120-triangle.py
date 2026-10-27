class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]
        for row in reversed(triangle[:-1]):
            dp = [v + min(dp[i], dp[i + 1]) for i, v in enumerate(row)]
        return dp[0]
