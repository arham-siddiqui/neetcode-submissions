class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        place = 0
        count=0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[place] = nums[i-1]
                count+=1
                place+=1
            if nums[i] == nums[i-1]:
                continue
        nums[place] = nums[-1]
        
        return count+1