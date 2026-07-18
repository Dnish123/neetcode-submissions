class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned =""

        for ch in s:
            if ch.isalnum():
                cleaned +=ch.lower()
        temp = cleaned[::-1]
        if cleaned != temp:
            return False
            
        return True
            
