class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  
        for i, temp in enumerate(temperatures):
            # While stack is not empty and current temp is warmer than the top of stack
            while stack and temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                answer[prev_idx] = i - prev_idx
            
            # Push current index onto stack
            stack.append(i)

        return answer