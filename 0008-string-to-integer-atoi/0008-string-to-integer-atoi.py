class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign, i = 1, 0
        if s and s[0] in "+-":
            sign = -1 if s[0] == "-" else 1
            i = 1
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        return max(-2**31, min(2**31 - 1, sign * num))
