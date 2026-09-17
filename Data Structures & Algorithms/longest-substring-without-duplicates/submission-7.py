class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:

        res=0
        n=len(nums)
        if n==1  : return 1
        for i in range(n):
            s=set()
            count=0
            for j in range(i,n):
                if nums[j] in s:
                    break
                else:
                    s.add(nums[j])
                    count+=1
            res=max(res,count)
            s.clear()
        return res

        