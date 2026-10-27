class Solution:
    def postorderTraversal(self, root) -> list[int]:
        res, stack = [], [root] if root else []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]
