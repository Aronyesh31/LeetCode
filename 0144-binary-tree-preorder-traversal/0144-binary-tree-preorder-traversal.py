class Solution:
    def preorderTraversal(self, root) -> list[int]:
        res, stack = [], [root] if root else []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
