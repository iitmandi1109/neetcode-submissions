class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right=0,len(people)-1
        ans=0
        while left<=right:
            val=people[left]+people[right]
            if val>limit:
                right-=1
            else:
                left+=1
                right-=1
            ans+=1
        return ans

        