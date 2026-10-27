from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = sum(v // 2 * 2 for v in Counter(s).values())
        return pairs + (pairs < len(s))
