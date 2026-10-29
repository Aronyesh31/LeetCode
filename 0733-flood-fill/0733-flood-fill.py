class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old = image[sr][sc]
        if old == color:
            return image
        m, n = len(image), len(image[0])
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            if 0 <= r < m and 0 <= c < n and image[r][c] == old:
                image[r][c] = color
                stack += [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        return image
