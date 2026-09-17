class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        v=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=len(nums)//3
        for key,values in d.items():
            if values>a:
                v.append(key)
        return v        