class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        halfway = -1

        while left <= right:
            halfway = (left + right) // 2
            if nums[halfway] == target:
                return halfway
            if nums[halfway] > target:
                right = halfway - 1
            else:
                left = halfway + 1
        
        return -1

        

        