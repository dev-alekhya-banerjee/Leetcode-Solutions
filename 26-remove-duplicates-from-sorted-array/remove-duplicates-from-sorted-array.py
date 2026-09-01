class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=i+1
        k=1
        while j<n:
            if nums[i]==nums[j]:
                j+=1
                continue
            else:
                nums[i+1]=nums[j]
                i+=1
                j+=1
                k+=1
        return k
