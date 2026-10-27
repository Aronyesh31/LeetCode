class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                keys = ((v, "r", r), (v, "c", c), (v, "b", r // 3, c // 3))
                if any(k in seen for k in keys):
                    return False
                seen.update(keys)
        return True
