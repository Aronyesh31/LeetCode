class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        res = []
        level = [root] if root else []
        while level:
            res.append([n.val for n in level])
            level = [c for n in level for c in (n.left, n.right) if c]
        return res
