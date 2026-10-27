class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        best = 0
        for i, h in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] >= h:
                start, top = stack.pop()
                best = max(best, top * (i - start))
            stack.append((start, h))
        return best
