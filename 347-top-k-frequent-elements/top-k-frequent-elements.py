import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        min_heap=[]
        d={}
        for val in nums:
            d[val]=d.get(val,0)+1
        items=list(d.items())
        for i in range(k):
            element,freq=items[i]
            heapq.heappush(min_heap,(freq,element))
        for i in range(k,len(items)):
            element,freq=items[i]
            if freq>min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,(freq,element))
        result=[]
        while min_heap:
            freq,element=heapq.heappop(min_heap)
            result.append(element)
        return result
