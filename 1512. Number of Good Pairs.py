class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        t= set(nums)
        out=0
        if t==len(nums):
            return 0
        else:
            for n in t:
                r=nums.count(n)
                out+= ((r)*(r-1))//2
            return out
        
