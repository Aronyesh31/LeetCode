class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        n = len(matrix[0])
        dp = [0] * (n + 1)
        best = 0
        for row in matrix:
            diag = 0
            for j in range(1, n + 1):
                tmp = dp[j]
                dp[j] = min(dp[j], dp[j - 1], diag) + 1 if row[j - 1] == "1" else 0
                best = max(best, dp[j])
                diag = tmp
        return best * best
