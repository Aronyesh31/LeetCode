class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        size = 1
        while size < n:
            size *= 2

        # Each node:
        # [product of entire segment % k, count of prefix products]
        tree = [[1 % k, [0] * k] for _ in range(2 * size)]

        # Build leaves
        for i in range(n):
            r = nums[i] % k
            tree[size + i] = [r, [0] * k]
            tree[size + i][1][r] = 1

        def merge(a, b):
            # Product of the whole combined segment
            product = (a[0] * b[0]) % k

            # Prefixes that end inside a
            count = a[1][:]

            # Prefixes that contain all of a
            # and then some prefix of b
            for r in range(k):
                new_r = (a[0] * r) % k
                count[new_r] += b[1][r]

            return [product, count]

        # Build segment tree
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        answer = []

        for index, value, start, x in queries:

            # -------------------------
            # Point update
            # -------------------------
            pos = size + index

            r = value % k

            tree[pos] = [r, [0] * k]
            tree[pos][1][r] = 1

            pos //= 2

            while pos > 0:
                tree[pos] = merge(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

            # -------------------------
            # Query [start, n - 1]
            # -------------------------
            left = [1 % k, [0] * k]
            right = [1 % k, [0] * k]

            l = size + start
            r = size + n

            while l < r:

                if l & 1:
                    left = merge(left, tree[l])
                    l += 1

                if r & 1:
                    r -= 1
                    right = merge(tree[r], right)

                l //= 2
                r //= 2

            result = merge(left, right)

            answer.append(result[1][x])

        return answer