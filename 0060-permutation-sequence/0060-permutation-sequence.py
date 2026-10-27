from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [str(i) for i in range(1, n + 1)]
        k -= 1
        out = []
        for i in range(n, 0, -1):
            idx, k = divmod(k, factorial(i - 1))
            out.append(digits.pop(idx))
        return "".join(out)
