class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size=len(nums)
        mi=min(nums)
        ma=max(nums)
        if ma<0:
            return 1
        for i in range(1,ma+1):
            if i not in nums:
                return i
        return ma+1
        