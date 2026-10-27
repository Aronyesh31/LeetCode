class Solution:
    def romanToInt(self, s: str) -> int:
        val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i, c in enumerate(s):
            if i + 1 < len(s) and val[c] < val[s[i + 1]]:
                total -= val[c]
            else:
                total += val[c]
        return total
