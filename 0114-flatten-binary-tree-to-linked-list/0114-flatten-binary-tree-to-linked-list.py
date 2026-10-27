class Solution:
    def flatten(self, root) -> None:
        node = root
        while node:
            if node.left:
                pre = node.left
                while pre.right:
                    pre = pre.right
                pre.right = node.right
                node.right, node.left = node.left, None
            node = node.right
