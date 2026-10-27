class Solution:
    def rightSideView(self, root) -> list[int]:
        res = []
        level = [root] if root else []
        while level:
            res.append(level[-1].val)
            level = [c for n in level for c in (n.left, n.right) if c]
        return res
