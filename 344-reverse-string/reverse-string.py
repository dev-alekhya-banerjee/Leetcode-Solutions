class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def stringRev(low: int,high: int) -> None:
            if low>=high:
                return
            s[low],s[high]=s[high],s[low]
            stringRev(low+1,high-1)
        stringRev(0,len(s)-1)