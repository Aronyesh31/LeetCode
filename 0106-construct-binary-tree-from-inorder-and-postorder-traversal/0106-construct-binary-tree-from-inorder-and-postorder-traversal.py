class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]):
        idx = {v: i for i, v in enumerate(inorder)}

        def build(lo, hi):
            if lo > hi:
                return None
            val = postorder.pop()
            node = TreeNode(val)
            node.right = build(idx[val] + 1, hi)
            node.left = build(lo, idx[val] - 1)
            return node

        return build(0, len(inorder) - 1)
