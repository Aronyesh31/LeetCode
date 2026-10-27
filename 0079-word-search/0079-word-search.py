class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r, c, k):
            if k == len(word):
                return True
            if not (0 <= r < m and 0 <= c < n) or board[r][c] != word[k]:
                return False
            ch, board[r][c] = board[r][c], "#"
            found = any(dfs(r + dr, c + dc, k + 1)
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            board[r][c] = ch
            return found

        return any(dfs(r, c, 0) for r in range(m) for c in range(n))
