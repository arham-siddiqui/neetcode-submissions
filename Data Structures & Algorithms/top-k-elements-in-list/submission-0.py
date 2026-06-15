class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {} # integer --> count
        arr = [[] for _ in range(len(nums)+1)]

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        for key in counts:
            arr[counts[key]].append(key)

        result = []

        for i in range(1, len(arr)):
            length = len(arr[-i])
            if length > 0:
                if k >= length:
                    result.extend(arr[-i])
                    k-=length
                else:
                    result.extend(arr[-i][0:k])
                    k=0
            if k==0:
                break
        
        return result
