class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for ch in s:

            # opening bracket
            if ch in "({[":
                stack.append(ch)

            # closing bracket
            else:

                # stack empty OR mismatch
                if not stack or stack[-1] != mapping[ch]:
                    return False

                stack.pop()

        return len(stack) == 0
        