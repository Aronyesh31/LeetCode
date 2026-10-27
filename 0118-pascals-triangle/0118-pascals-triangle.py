class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        for _ in range(numRows - 1):
            prev = res[-1]
            res.append([1] + [a + b for a, b in zip(prev, prev[1:])] + [1])
        return res
