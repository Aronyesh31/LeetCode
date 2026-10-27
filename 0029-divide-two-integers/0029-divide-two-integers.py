class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        q = 0
        for shift in range(31, -1, -1):
            if (b << shift) <= a:
                a -= b << shift
                q |= 1 << shift
        q = -q if neg else q
        return max(-2**31, min(2**31 - 1, q))
