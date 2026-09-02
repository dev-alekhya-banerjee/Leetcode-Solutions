class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        i=0
        j=n-1
        k=n-1
        while i<=j:
            ls=nums[i]**2
            rs=nums[j]**2
            if rs>ls:
                ans[k]=rs
                k-=1
                j-=1
            else:
                ans[k]=ls
                k-=1
                i+=1
        return ans



        