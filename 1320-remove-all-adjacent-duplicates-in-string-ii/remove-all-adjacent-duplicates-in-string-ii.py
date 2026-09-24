class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n=len(s)
        stack=[]
        for i in range(n):
            if not stack or stack[-1][0]!=s[i]:
                stack.append([s[i],1])
            else:
                stack[-1][1]+=1
            if stack[-1][1]==k:
                stack.pop()
        ans=[]
        for char,freq in stack:
            ans.append(char * freq)
        return "".join(ans)
