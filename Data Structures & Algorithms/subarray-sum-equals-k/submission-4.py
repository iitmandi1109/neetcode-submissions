class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Step 1: Build prefix sum array
        prefix = [0]*(n+1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Step 2: Use dictionary to count prefix sums
        freq = {}
        count = 0

        for p in prefix:
            required = p - k

            if required in freq:
                count += freq[required]
            freq[p] = freq.get(p, 0) + 1


        return count