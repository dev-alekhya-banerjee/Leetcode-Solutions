class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        max_area=float('-inf')
        while left<right:
            x=right-left
            y=min(height[left],height[right])
            area=x*y
            max_area=max(max_area,area)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return max_area

        