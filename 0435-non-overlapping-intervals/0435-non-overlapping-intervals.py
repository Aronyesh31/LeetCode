class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end, keep = float("-inf"), 0
        for s, e in intervals:
            if s >= end:
                keep += 1
                end = e
        return len(intervals) - keep
