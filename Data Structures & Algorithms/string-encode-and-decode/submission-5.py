class Solution:

    def encode(self, strs: List[str]) -> str:

        output = ""
        for i in range(len(strs)):
            length = len(strs[i])
            output += str(length) + "#" + strs[i]
        
        return output

    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        output = []
        i = 0
        while i < len(s):

            j = i

            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])
            output.append(s[j + 1 : j + length + 1])
            i = j + length + 1
        
        return output
        
            

