class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        dp = [0] + [float("inf")] * n
        for i in range(1, n + 1):
            for s in squares:
                if s > i:
                    break
                dp[i] = min(dp[i], dp[i - s] + 1)
        return dp[n]
