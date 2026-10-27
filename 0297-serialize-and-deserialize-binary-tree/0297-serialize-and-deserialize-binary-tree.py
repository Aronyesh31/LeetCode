class Codec:
    def serialize(self, root):
        out = []

        def dfs(node):
            if not node:
                out.append("#")
                return
            out.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(out)

    def deserialize(self, data):
        it = iter(data.split(","))

        def build():
            v = next(it)
            if v == "#":
                return None
            node = TreeNode(int(v))
            node.left = build()
            node.right = build()
            return node

        return build()
