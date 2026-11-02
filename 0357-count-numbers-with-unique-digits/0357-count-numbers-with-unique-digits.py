class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1

        count = 10
        unique = 9
        available = 9

        for i in range(2, n + 1):
            unique *= available
            count += unique
            available -= 1

        return count