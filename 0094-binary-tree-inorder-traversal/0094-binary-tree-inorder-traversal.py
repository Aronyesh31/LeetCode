class Solution:
    def inorderTraversal(self, root) -> list[int]:
        res, stack, node = [], [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
