class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowels = set("aeiouAEIOU")
        l, r = 0, len(chars) - 1
        while l < r:
            if chars[l] not in vowels:
                l += 1
            elif chars[r] not in vowels:
                r -= 1
            else:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
        return "".join(chars)
