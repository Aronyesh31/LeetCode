class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res, cols = [], []
        used_c, used_d1, used_d2 = set(), set(), set()

        def dfs(r):
            if r == n:
                res.append(["." * c + "Q" + "." * (n - c - 1) for c in cols])
                return
            for c in range(n):
                if c in used_c or r - c in used_d1 or r + c in used_d2:
                    continue
                used_c.add(c); used_d1.add(r - c); used_d2.add(r + c)
                cols.append(c)
                dfs(r + 1)
                cols.pop()
                used_c.remove(c); used_d1.remove(r - c); used_d2.remove(r + c)

        dfs(0)
        return res
