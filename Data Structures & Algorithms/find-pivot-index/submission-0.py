class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        curr = 0
        total = 0
        for i in range(len(nums)):
            total+=nums[i]
        
        for i in range(len(nums)):
            if (curr == total - nums[i] - curr):
                return i
            curr = curr + nums[i]
        
        return -1