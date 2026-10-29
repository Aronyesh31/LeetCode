from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        need, window = Counter(s1), Counter(s2[:k])
        if window == need:
            return True
        for i in range(k, len(s2)):
            window[s2[i]] += 1
            window[s2[i - k]] -= 1
            if window == need:
                return True
        return False
