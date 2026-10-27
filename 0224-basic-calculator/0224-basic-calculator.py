class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res, num, sign = 0, 0, 1
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                res += sign * num
                num, sign = 0, 1 if c == "+" else -1
            elif c == "(":
                stack.append((res, sign))
                res, sign = 0, 1
            elif c == ")":
                res += sign * num
                num = 0
                prev, prev_sign = stack.pop()
                res = prev + prev_sign * res
        return res + sign * num
