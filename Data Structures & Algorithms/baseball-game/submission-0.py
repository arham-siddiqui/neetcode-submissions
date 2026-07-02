class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        runningSum = 0

        for n in operations:
            
            if n == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
                runningSum += int(stack[-1])
                continue
            
            if n == "D":
                stack.append(int(stack[-1])*2)
                runningSum += int(stack[-1])
                continue
            
            if n == "C":
                runningSum -= int(stack[-1])
                stack.pop(-1)
                continue
            
            stack.append(int(n))
            runningSum += int(n)
        
        return runningSum

            

            
