class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters=[]
        result=[]
        n=len(digits)
        if n==0:
            return []
        d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def combinations(i):
            if i==n:
                result.append("".join(letters))
                return
            t=d[digits[i]]
            for char in t:
                letters.append(char)
                combinations(i+1)
                letters.pop()
            return
        combinations(0)
        return result
        