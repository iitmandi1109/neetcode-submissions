class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        
        # count frequency
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        
        # sort based on frequency
        sorted_items = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
        
        # take top k elements
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])  # key
        
        return result
        