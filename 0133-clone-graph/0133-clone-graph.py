class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        copies = {node: Node(node.val)}
        stack = [node]
        while stack:
            cur = stack.pop()
            for nb in cur.neighbors:
                if nb not in copies:
                    copies[nb] = Node(nb.val)
                    stack.append(nb)
                copies[cur].neighbors.append(copies[nb])
        return copies[node]
