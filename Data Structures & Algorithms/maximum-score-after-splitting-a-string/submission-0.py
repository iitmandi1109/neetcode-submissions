class Solution:
    def maxScore(self, s: str) -> int:
        res = 0

        for i in range(len(s)-1):   
            left = s[:i+1].count('0')
            right = s[i+1:].count('1')
            res = max(res, left + right)

        return res

        