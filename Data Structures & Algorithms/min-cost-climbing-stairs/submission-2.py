class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, n):
            dp[i] = nums[i] + min(dp[i-1], dp[i-2])

        return min(dp[n-1], dp[n-2])
        