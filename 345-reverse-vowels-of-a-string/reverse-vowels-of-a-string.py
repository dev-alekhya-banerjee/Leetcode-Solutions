class Solution:
    def reverseVowels(self, s: str) -> str:
        d={'a', 'e', 'i', 'o', 'u','A','E','I','O','U'}
        l=[]
        for char in s:
            l.append(char)
        i=0
        j=len(l)-1
        while i<j:
            while i<j and l[j] not in d:
                j-=1
            while i<j and l[i] not in d:
                i+=1
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1
        return "".join(l)