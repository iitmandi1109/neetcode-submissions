class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1=len(word1)
        s2=len(word2)
        loop=min(s1,s2)
        val=""
        for i in range(loop):
            val=val+word1[i]
            val=val+word2[i]
        
        if s1>s2:
            val=val+word1[loop::]
        else:
            val=val+word2[loop::]
        return val
        

        