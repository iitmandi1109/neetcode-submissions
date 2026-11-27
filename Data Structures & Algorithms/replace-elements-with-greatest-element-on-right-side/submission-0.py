class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l=[]
        l.append(-1)
        last=arr[-1]
        for i in range(len(arr)-1,0,-1):
            last=max(last,arr[i])
            l.append(last)
        l.reverse()
        return l
        