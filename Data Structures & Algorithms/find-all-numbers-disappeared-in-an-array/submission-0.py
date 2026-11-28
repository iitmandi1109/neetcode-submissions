class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=len(nums)
        l1=[]
        for i in range(1,l+1):
            if i not in nums:
                l1.append(i)
       
        return l1
        