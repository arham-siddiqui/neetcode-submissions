class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        parsed = ""

        for c in s:
            if c in chars:
                parsed += c.lower()
        
        for left in range(len(parsed) // 2):
            right = len(parsed) - left - 1
            if parsed[right] != parsed[left]:
                return False
        
        return True