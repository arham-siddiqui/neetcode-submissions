class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1
        curr = 0

        while right < len(prices):
            
            if prices[right] <= prices[left]:
                left = right
                right += 1
            elif prices[right] > prices[left]:
                curr = max(curr, prices[right]-prices[left])
                right += 1
        
        return curr

        
