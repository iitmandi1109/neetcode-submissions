class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        j=0
        count=1
        for i in range(1,len(nums)):
            if nums[i]==nums[j]:
                count+=1
            else:
                count-=1
            if count==0:
                j=i
                count=1
        res=nums[j]
        count=0
        for i in nums:
            if i==res:
                count+=1
        if count>=len(nums)/2:
            return res
        
        