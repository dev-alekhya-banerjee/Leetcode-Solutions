class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        D={}
        zeroes=0
        ones=0
        max_length=0
        for i in range(n):
            if nums[i]==0:
                zeroes+=1
            else:
                ones+=1
            diff=zeroes-ones
            if diff==0:
                max_length=max(max_length,i+1)
                continue
            if diff in D:
                length=i-D[diff]
                max_length=max(length,max_length)
            else:
                D[diff]=i
        return max_length

        