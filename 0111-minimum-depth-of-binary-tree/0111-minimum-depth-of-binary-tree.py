class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0
        level, depth = [root], 1
        while level:
            nxt = []
            for n in level:
                if not n.left and not n.right:
                    return depth
                nxt += [c for c in (n.left, n.right) if c]
            level, depth = nxt, depth + 1
        return depth
