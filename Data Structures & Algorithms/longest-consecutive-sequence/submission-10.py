class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for num in s:
            # only start if it's the beginning of a sequence
            if num - 1 not in s:
                current = num
                count = 1

                while current + 1 in s:
                    current += 1
                    count += 1

                res = max(res, count)

        return res