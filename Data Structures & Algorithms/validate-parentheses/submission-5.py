class Solution:
    def isValid(self, s: str) -> bool:
        openStack = []
        closedStack = []
        counterPart = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        for p in s:
            if p == '(' or p == '{' or p == '[':
                openStack.append(p)
                closedStack.append(counterPart[p])
            if p == ')' or p == '}' or p == ']':
                if len(closedStack) == 0:
                    return False
                if p == closedStack[-1]:
                    del closedStack[-1]
                    del openStack[-1]
                else:
                    return False

        if len(openStack) == 0 and len(closedStack) == 0:
            return True 
                   
        return False
