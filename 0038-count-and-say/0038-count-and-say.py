from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            s = "".join(f"{len(list(g))}{d}" for d, g in groupby(s))
        return s
