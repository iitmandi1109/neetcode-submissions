class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1=len(s)
        t1=len(t)
        if s1==0:
            return True
        j=0
        for i in range(t1):
            if t[i]==s[j]:
                j+=1
            if j==s1:
                return True
        print(s1,j)
        return j==s1
        