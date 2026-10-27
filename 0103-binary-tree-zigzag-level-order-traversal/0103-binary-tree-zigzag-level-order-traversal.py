class Solution:
    def zigzagLevelOrder(self, root) -> list[list[int]]:
        res = []
        level = [root] if root else []
        while level:
            vals = [n.val for n in level]
            res.append(vals if len(res) % 2 == 0 else vals[::-1])
            level = [c for n in level for c in (n.left, n.right) if c]
        return res
