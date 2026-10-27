class Solution:
    def pathSum(self, root, targetSum: int) -> list[list[int]]:
        res, path = [], []

        def dfs(node, remain):
            if not node:
                return
            path.append(node.val)
            remain -= node.val
            if not node.left and not node.right and remain == 0:
                res.append(path[:])
            dfs(node.left, remain)
            dfs(node.right, remain)
            path.pop()

        dfs(root, targetSum)
        return res
