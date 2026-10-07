class Solution:
    def reverse(self, x):

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        while x > 0:
            digit = x % 10
            x = x // 10

            # Check overflow before result * 10 + digit
            if result > INT_MAX // 10:
                return 0

            if result == INT_MAX // 10 and digit > 7:
                return 0

            result = result * 10 + digit

        return sign * result
