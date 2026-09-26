class Solution:
    def maxPathScore(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                value = grid[i][j]
                cost = 0 if value == 0 else 1
                score = value

                for c in range(k + 1):
                    if c < cost:
                        continue

                    previous = -1

                    if i > 0:
                        previous = max(previous, dp[i - 1][j][c - cost])

                    if j > 0:
                        previous = max(previous, dp[i][j - 1][c - cost])

                    if previous != -1:
                        dp[i][j][c] = previous + score

        answer = max(dp[m - 1][n - 1])

        return answer if answer != -1 else -1