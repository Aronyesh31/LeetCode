class Solution:
    def binaryTreePaths(self, root) -> list[str]:
        res = []

        def dfs(node, path):
            path = path + [str(node.val)]
            if not node.left and not node.right:
                res.append("->".join(path))
            for child in (node.left, node.right):
                if child:
                    dfs(child, path)

        dfs(root, [])
        return res
