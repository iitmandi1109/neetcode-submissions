class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = []
        def backtrack(i, curr):
            if i == len(nums):
                l.append(curr[:])
                return
            backtrack(i + 1, curr)
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
        backtrack(0, [])
        return l

        