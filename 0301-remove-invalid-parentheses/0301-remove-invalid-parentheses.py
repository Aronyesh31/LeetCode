class Solution:
    def removeInvalidParentheses(self, s):

        def isValid(x):
            count = 0

            for ch in x:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        current = set([s])

        while True:

            # Check all strings at this removal level
            answer = []

            for string in current:
                if isValid(string):
                    answer.append(string)

            # If we found valid strings, this is the minimum
            # number of removals.
            if answer:
                return answer

            # Generate next level
            next_level = set()

            for string in current:

                for i in range(len(string)):

                    # Only remove parentheses
                    if string[i] != '(' and string[i] != ')':
                        continue

                    new_string = string[:i] + string[i + 1:]

                    next_level.add(new_string)

            current = next_level
