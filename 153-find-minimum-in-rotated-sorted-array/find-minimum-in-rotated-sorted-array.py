class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        index=0
        high=n-1
        while low<=high:
            guess=(low+high)//2
            if nums[guess]<=nums[n-1]: #first occurence of part 1
                index=guess
                high=guess-1
            else:
                low=guess+1
        return nums[index]
        