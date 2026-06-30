class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        runningMax = 0
        for i in range(1, len(height)):
            runningMax = max(height[i-1], runningMax)
            maxLeft[i] = runningMax
        maxLeft[-1] = runningMax
        
        runningMax = 0
        for i in range(len(height)-2, 0, -1):
            runningMax = max(height[i+1], runningMax)
            maxRight[i] = runningMax
        maxRight[0] = runningMax

        waterTotal = 0
        for i in range(len(height)):
            waterTotal += max((min(maxLeft[i], maxRight[i]) - height[i]), 0)
        
        return waterTotal
