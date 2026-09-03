class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        mini=float('inf')
        ans=[]
        for i in range(n):
            left=i+1
            right=n-1
            while left<right:
                the_sum=nums[i]+nums[left]+nums[right]
                diff=abs(target-the_sum)
                if diff<mini:
                    mini=diff
                    current_sum=the_sum
                if the_sum>target:
                    right-=1
                else:
                    left+=1
        return current_sum
        