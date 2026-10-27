class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [1] + [a + b for a, b in zip(row, row[1:])] + [1]
        return row
