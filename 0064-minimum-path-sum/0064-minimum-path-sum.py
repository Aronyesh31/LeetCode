class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        dp = [float("inf")] * n
        dp[0] = 0
        for row in grid:
            dp[0] += row[0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + row[j]
        return dp[-1]
