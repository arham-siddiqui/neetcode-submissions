class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = set()
        left = 0
        maxSub = 0

        for i in range(len(s)):
            if s[i] in window:
                maxSub = max(maxSub, i - left)
                print(window, maxSub)
                while s[i] in window:
                    window.remove(s[left])
                    left += 1
            window.add(s[i])
        
        return max(maxSub, len(window))
