class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def backtrack(s):
            if len(s) == n:
                res.append(s)
                return

            for ch in "abc":
                if not s or s[-1] != ch:
                    backtrack(s + ch)

        backtrack("")

        if len(res) < k:
            return ""

        return res[k - 1]