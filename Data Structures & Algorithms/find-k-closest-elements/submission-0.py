class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i=0
        j=k
        num=arr[i:j]
        res=0
        for i in num:
            val=abs(x-i)
            res+=val
        ans=res
        l=0
        m=k
        for i in range(0,len(arr)-k):
            pre=abs(x-arr[i])
            post=abs(x-arr[i+k])
            res-=pre
            res+=post
            if res<ans:
                l=i+1
                m=i+k+1
                ans=res
        return arr[l:m]    

            
            
        

        