from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        left = top = 0
        for right, c in enumerate(s):
            count[c] += 1
            top = max(top, count[c])
            if right - left + 1 - top > k:
                count[s[left]] -= 1
                left += 1
        return len(s) - left
