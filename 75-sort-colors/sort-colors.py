class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        low=0
        mid=0
        high=n-1
        while mid<=high:
            if nums[mid]==1: #best case
                mid+=1
            elif nums[mid]==0:
                temp=nums[mid]
                nums[mid]=nums[low]
                nums[low]=temp
                low+=1
                mid+=1
            else:
                temp=nums[high]
                nums[high]=nums[mid]
                nums[mid]=temp
                high-=1

        