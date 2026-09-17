class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        # Count frequency
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        # Convert to list of (number, frequency)
        s = []

        for x, count in freq.items():
            s.append((x, count))

        # Sort by frequency
        s.sort(key=lambda x: x[1], reverse=True)

        # Take top k
        ans = []

        for i in range(k):
            ans.append(s[i][0])

        return ans
        