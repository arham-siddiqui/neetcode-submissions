class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        parsed = ""

        for c in s:
            if c in chars:
                parsed += c.lower()
        
        left = 0
        right = len(parsed) - 1

        while (left < right):
            if parsed[left] != parsed[right]:
                return False
            left += 1
            right -= 1
        
        return True