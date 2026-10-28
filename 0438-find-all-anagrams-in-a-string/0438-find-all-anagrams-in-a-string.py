from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        need, window = Counter(p), Counter()
        res, k = [], len(p)
        for i, c in enumerate(s):
            window[c] += 1
            if i >= k:
                window[s[i - k]] -= 1
                if window[s[i - k]] == 0:
                    del window[s[i - k]]
            if window == need:
                res.append(i - k + 1)
        return res
