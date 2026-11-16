class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_round = []
            for i in range(0, len(s), k):
                # Sum the digits of the current chunk
                chunk_sum = sum(int(ch) for ch in s[i:i + k])
                next_round.append(str(chunk_sum))
            # Merge the groups together to form the new string
            s = "".join(next_round)
        return s