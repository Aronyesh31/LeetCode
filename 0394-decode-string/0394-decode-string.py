class Solution:
    def decodeString(self, s: str) -> str:
        stack, cur, num = [], "", 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((cur, num))
                cur, num = "", 0
            elif c == "]":
                prev, k = stack.pop()
                cur = prev + cur * k
            else:
                cur += c
        return cur
