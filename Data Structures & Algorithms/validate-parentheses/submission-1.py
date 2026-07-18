class Solution:
    def isValid(self, s: str) -> bool:
                stack = []

                mapping = {

                        ')':'(',
                        ']':'[',
                        '}':'{'

                        }

                for ch in s: #for opening parenthesis
                        if ch in '([{':
                                stack.append(ch)
                
                        else:
                                if not stack or stack[-1] != mapping[ch]:
                                        return False
                        
                                stack.pop()
                
                
                return len(stack) == 0
        

        