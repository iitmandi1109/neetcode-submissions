class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        l = [nums[0]]
        for i in range(1, len(nums)):
            while l and l[-1] > 0 and nums[i] < 0:
                a = abs(l[-1])
                b = abs(nums[i])
                if a < b:
                    l.pop()
                    continue
                elif a == b:
                    l.pop()
                    nums[i] = 0
                else:  # a > b
                    nums[i] = 0
                break
            if nums[i] != 0:
                l.append(nums[i])
        return l
