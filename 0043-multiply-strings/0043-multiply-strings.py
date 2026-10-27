class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                p = int(num1[i]) * int(num2[j]) + res[i + j + 1]
                res[i + j + 1] = p % 10
                res[i + j] += p // 10
        s = "".join(map(str, res)).lstrip("0")
        return s or "0"
