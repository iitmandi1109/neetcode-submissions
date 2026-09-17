class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size=len(s1)
        new=sorted(s1)
        size2=len(s2)
        for i in range(size2-size+1):
            st=s2[i:i+size]
            if sorted(st)==new:
                return True
        return False
        