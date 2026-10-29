class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        best = 0
        for r in range(m):
            for c in range(n):
                if not grid[r][c]:
                    continue
                grid[r][c] = 0
                stack, area = [(r, c)], 0
                while stack:
                    i, j = stack.pop()
                    area += 1
                    for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]:
                            grid[ni][nj] = 0
                            stack.append((ni, nj))
                best = max(best, area)
        return best
