class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(x):
            out = []
            for c in x:
                if c == "#":
                    if out:
                        out.pop()
                else:
                    out.append(c)
            return out

        return build(s) == build(t)
