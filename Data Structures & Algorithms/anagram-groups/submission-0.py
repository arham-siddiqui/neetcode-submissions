class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {} # map characters(STR) to wordList(LIST)

        for word in strs:
            chars = [0] * 26

            for letter in word:
                chars[ord(letter) - ord("a")] += 1
            
            # chars --> [0, 0, 0, 1, 0, 1, 0, 0, 1]
            key = str(chars)

            if key not in result:
                result[key] = []
                result[key].append(word)
            else:
                result[key].append(word)

        return list(result.values())



        
        

