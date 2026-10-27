class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while True:
            mid = (lo + hi) // 2
            g = guess(mid)
            if g == 0:
                return mid
            if g < 0:
                hi = mid - 1
            else:
                lo = mid + 1
