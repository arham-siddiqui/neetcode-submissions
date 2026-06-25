class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        size = len(nums)
        count=0
        left = 0
        right = len(nums)-1
        curr = nums[left]
        while left < right:
            left += 1
            if curr == nums[left]:
                del nums[left]
                left-=1
                right-=1
                count+=1
            curr = nums[left]
        
        return size-count