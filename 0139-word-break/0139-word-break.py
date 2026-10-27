class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            dp[i] = any(dp[j] and s[j:i] in words for j in range(i))
        return dp[-1]
