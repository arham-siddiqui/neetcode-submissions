class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        arr = collections.defaultdict(set)
        isStart = True
        startingValues = []

        # convert to hashset
        for i in range(len(nums)):
            arr[0].add(nums[i])

        # obtain starting values
        for n in nums:
            if (n-1) not in arr[0]:
                startingValues.append(n)

        # build lists of starting values
        output = 0
        for x in startingValues:
            curr = [x]

            while True:
                if (curr[-1]+1) in arr[0]:
                    curr.append(curr[-1]+1)
                else:
                    output = max(output, len(curr))
                    break
        return output
            

        
