class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        se=set()
        for i in range(len(nums)):
            st=set()
            for j in range(i+1,len(nums)):
                target=-nums[i]-nums[j]
                if target in st:
                    val=tuple(sorted([nums[i],nums[j],target]))
                    se.add(val)
                st.add(nums[j])
        return list(se)

