class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda p: p[1])
        arrows, end = 0, float("-inf")
        for s, e in points:
            if s > end:
                arrows += 1
                end = e
        return arrows
