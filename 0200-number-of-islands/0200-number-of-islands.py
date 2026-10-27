class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def sink(r, c):
            stack = [(r, c)]
            grid[r][c] = "0"
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        stack.append((nr, nc))

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    sink(r, c)
                    count += 1
        return count
