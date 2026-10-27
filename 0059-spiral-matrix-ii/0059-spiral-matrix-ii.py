class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        grid = [[0] * n for _ in range(n)]
        r = c = 0
        dr, dc = 0, 1
        for v in range(1, n * n + 1):
            grid[r][c] = v
            nr, nc = r + dr, c + dc
            if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc]:
                dr, dc = dc, -dr
            r, c = r + dr, c + dc
        return grid
