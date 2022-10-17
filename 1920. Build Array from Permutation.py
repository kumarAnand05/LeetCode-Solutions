class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for n in range(len(nums)):
            t= nums[nums[n]]
            ans.append(t)
        return ans
    
