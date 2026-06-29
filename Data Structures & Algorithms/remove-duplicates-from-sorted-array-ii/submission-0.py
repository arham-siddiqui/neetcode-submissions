class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        counter = 0
        k=0

        while right < len(nums):
            curr = nums[right]

            while True:
                if right >= len(nums) or nums[right] != curr:
                    break
                counter += 1
                right += 1
            
            if counter >= 2:
                nums[left], nums[left+1] = curr, curr
                k += 2
                left += 2
            elif counter < 2:
                nums[left] = curr
                k += 1
                left += 1

            counter = 0
        
        return k
        
