class Solution:
    def numDecodings(self, s: str) -> int:
        prev, cur = 0, 1
        for i, c in enumerate(s):
            nxt = cur if c != "0" else 0
            if i and "10" <= s[i - 1:i + 1] <= "26":
                nxt += prev
            prev, cur = cur, nxt
        return cur
