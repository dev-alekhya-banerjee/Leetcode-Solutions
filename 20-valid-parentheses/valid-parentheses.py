class Solution:
    def isValid(self, s: str) -> bool:
        bracketmap={')':'(','}':'{',']':'['}
        stack=[]
        for char in s: #bracket is open
            if char in bracketmap: #bracket is close
                if stack and stack[-1]==bracketmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if len(stack)==0:
            return True
        else:
            return False