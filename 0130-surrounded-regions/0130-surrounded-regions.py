class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m, n = len(board), len(board[0])
        stack = [(r, c) for r in range(m) for c in range(n)
                 if (r in (0, m - 1) or c in (0, n - 1)) and board[r][c] == "O"]
        while stack:
            r, c = stack.pop()
            if 0 <= r < m and 0 <= c < n and board[r][c] == "O":
                board[r][c] = "S"
                stack += [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for row in board:
            for c in range(n):
                row[c] = "O" if row[c] == "S" else "X"
