class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        for row in obstacleGrid:
            for j in range(n):
                if row[j]:
                    dp[j] = 0
                elif j:
                    dp[j] += dp[j - 1]
        return dp[-1]
