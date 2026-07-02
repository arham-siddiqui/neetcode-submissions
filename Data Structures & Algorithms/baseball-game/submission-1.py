class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for n in operations:
            
            if n == "+":
                stack.append(stack[-1] + stack[-2])
                continue
            
            if n == "D":
                stack.append(stack[-1]*2)
                continue
            
            if n == "C":
                stack.pop(-1)
                continue
            
            stack.append(int(n))
        
        return sum(stack)