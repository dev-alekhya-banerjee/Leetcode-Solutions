import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap=[]
        d={}
        for char in s:
            d[char]=d.get(char,0)+1
        for char,freq in d.items():
            heapq.heappush(max_heap,(-freq,char))
        ans=[]
        prev_freq=0
        prev_char=0
        while max_heap:
            neg_freq,char=heapq.heappop(max_heap)
            freq=-neg_freq
            ans.append(char)
            freq-=1
            if prev_freq>0:
                heapq.heappush(max_heap,(-prev_freq,prev_char))
            prev_freq=freq
            prev_char=char
        if len(ans)==len(s):
            return "".join(ans)
        else:
            return ""