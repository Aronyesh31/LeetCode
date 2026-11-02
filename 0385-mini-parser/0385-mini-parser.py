class Solution:
    def deserialize(self, s):
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ""

        for ch in s:
            if ch == '[':
                ni = NestedInteger()

                if stack:
                    stack[-1].add(ni)

                stack.append(ni)

            elif ch == ',' or ch == ']':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""

                if ch == ']':
                    result = stack.pop()

            else:
                num += ch

        return result