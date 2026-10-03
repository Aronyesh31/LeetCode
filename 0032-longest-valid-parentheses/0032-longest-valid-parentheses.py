class Solution:
    def longestValidParentheses(self, s):
        left = 0
        right = 0
        ans = 0

        # Left to right
        for ch in s:
            if ch == '(':
                left += 1
            else:
                right += 1

            if left == right:
                ans = max(ans, 2 * right)
            elif right > left:
                left = 0
                right = 0

        left = 0
        right = 0

        # Right to left
        for ch in reversed(s):
            if ch == '(':
                left += 1
            else:
                right += 1

            if left == right:
                ans = max(ans, 2 * left)
            elif left > right:
                left = 0
                right = 0

        return ans
        