class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        n=len(intervals)
        List=[]
        insert=False
        start=newInterval[0]
        for i in range(n):
            if start<=intervals[i][0] and insert==False:
                List.append(newInterval)
                insert=True
            List.append(intervals[i])
        if insert==False:
            List.append(newInterval)
        ans=[]
        n1=len(List)
        start1=List[0][0]
        end1=List[0][1]
        for i in range(1,n1):
            start2=List[i][0]
            end2=List[i][1]
            if end1>=start2:
                start1=start1
                end1=max(end1,end2)
                continue
            ans.append([start1,end1])
            start1=start2
            end1=end2
        ans.append([start1,end1])
        return ans



        