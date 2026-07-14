class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = len(prices)-1

        curr = 0

        for i in range(len(prices)-1):

            while left < right:
                if prices[right] - prices[left] > curr:
                    curr = prices[right] - prices[left]
                right -= 1

            right = len(prices)-1
            left += 1
        
        return curr