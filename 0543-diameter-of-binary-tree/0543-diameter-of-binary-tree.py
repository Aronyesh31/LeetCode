class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        best = 0

        def depth(node):
            nonlocal best
            if not node:
                return 0
            l, r = depth(node.left), depth(node.right)
            best = max(best, l + r)
            return 1 + max(l, r)

        depth(root)
        return best
