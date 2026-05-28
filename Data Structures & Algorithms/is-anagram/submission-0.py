class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap letter -> count (r: 2, a: 2, ...)
        firstMap = dict()
        
        for i in s:
            if i in firstMap.keys():
                firstMap[i] += 1
            else:
                firstMap[i] = 1

        secondMap = dict()
        
        for i in t:
            if i in secondMap.keys():
                secondMap[i] += 1
            else:
                secondMap[i] = 1
        
        if (dict(sorted(firstMap.items())) == (dict(sorted(secondMap.items())))):
            return True
        else:
            return False

        