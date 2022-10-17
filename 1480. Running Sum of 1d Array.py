class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new= []
        t=0
        for n in range(len(nums)):
            t= t+nums[n]
            new.append(t)
        return new
