class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1, 2, 4, 6]
        # products = [1, 2, 8, 48]
        count=0
        index=0
        product = 1
        for i in range(len(nums)):
            if (nums[i] == 0):
                count+=1
                index = i
                if count >= 2:
                    return [0] * len(nums)
                continue
            product = product * nums[i]

        if count == 1:
            output = [0] * len(nums)
            output[index] = product
            return output
        
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = product // nums[i]
        
        return output
            
        
        