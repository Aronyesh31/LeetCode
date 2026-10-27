class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = {i for i, row in enumerate(matrix) for v in row if v == 0}
        cols = {j for row in matrix for j, v in enumerate(row) if v == 0}
        for i, row in enumerate(matrix):
            for j in range(len(row)):
                if i in rows or j in cols:
                    row[j] = 0
