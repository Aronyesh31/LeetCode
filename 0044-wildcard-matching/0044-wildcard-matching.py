class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        star, match = -1, 0
        while i < len(s):
            if j < len(p) and p[j] in (s[i], "?"):
                i += 1
                j += 1
            elif j < len(p) and p[j] == "*":
                star, match = j, i
                j += 1
            elif star != -1:
                j = star + 1
                match += 1
                i = match
            else:
                return False
        return all(c == "*" for c in p[j:])
