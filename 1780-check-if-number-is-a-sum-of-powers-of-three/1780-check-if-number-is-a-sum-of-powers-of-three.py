class Solution:
    def checkPowersOfThree(self, n):
        while n > 0:
            if n % 3 == 2:
                return False

            n = n // 3

        return True