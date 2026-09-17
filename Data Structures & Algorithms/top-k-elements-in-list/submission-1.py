class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

        sorted_items = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])  # key
        return result
        