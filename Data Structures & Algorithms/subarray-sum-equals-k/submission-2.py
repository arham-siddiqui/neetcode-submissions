class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        subArraySum = 0
        prefixSum = {0: 1}
        count=0

        for i in nums:
            subArraySum += i
            necessary = subArraySum - k

            count += prefixSum.get(necessary, 0)
            prefixSum[subArraySum] = 1 + prefixSum.get(subArraySum, 0)

        
        return count