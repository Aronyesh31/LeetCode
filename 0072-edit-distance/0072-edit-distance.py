class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word2)
        prev = list(range(m + 1))
        for i, a in enumerate(word1, 1):
            cur = [i] + [0] * m
            for j, b in enumerate(word2, 1):
                if a == b:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(prev[j - 1], prev[j], cur[j - 1])
            prev = cur
        return prev[m]
