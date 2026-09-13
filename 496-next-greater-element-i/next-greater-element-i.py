class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stack = []
        d = {}
        
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
                
            if stack:
                d[nums2[i]] = stack[-1]
            else:
                d[nums2[i]] = -1
                
            stack.append(nums2[i])
            
        ans = []
        for num in nums1:
            ans.append(d[num])  
            
        return ans