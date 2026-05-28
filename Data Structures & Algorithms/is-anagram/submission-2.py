class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap letter -> count (r: 2, a: 2, ...)
        # in this approach i want to have just one hashmap, 
        # and in each iteration add and subtract characters
        # if its equal, all values should equal 0

        myMap = {}

        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            myMap[s[i]] = myMap.get(s[i], 0) + 1
            myMap[t[i]] = myMap.get(t[i], 0) - 1

        return all(v == 0 for v in myMap.values())

        