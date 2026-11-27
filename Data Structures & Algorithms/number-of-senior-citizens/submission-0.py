class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans=0
        for i in details:
            a=int(i[11:13])
            if a>60:
                ans+=1
        return ans