class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        idx = {v: i for i, v in enumerate(inorder)}
        it = iter(preorder)

        def build(lo, hi):
            if lo > hi:
                return None
            val = next(it)
            node = TreeNode(val)
            node.left = build(lo, idx[val] - 1)
            node.right = build(idx[val] + 1, hi)
            return node

        return build(0, len(inorder) - 1)
