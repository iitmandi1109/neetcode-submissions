class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1]
        res = 0

        for ch in s:
            if ch == ' ' and res == 0:
                continue
            elif ch != ' ':
                res += 1
            else:
                break

        return res