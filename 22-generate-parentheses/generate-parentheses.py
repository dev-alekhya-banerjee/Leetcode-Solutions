class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        temp=[]
        result=[]
        def Parenthesis(opening,closing):
            if opening==n and closing==n: #Base Case
                result.append("".join(temp)) #output: String inside list
                return 
            if opening<n:#Open
                temp.append('(') #Take
                Parenthesis(opening+1,closing)
                temp.pop() #Backtrack #Not take
            if closing<opening:#Close
                temp.append(')') #Take
                Parenthesis(opening,closing+1)
                temp.pop() #Backtrack #Not take
        Parenthesis(0,0)
        return result