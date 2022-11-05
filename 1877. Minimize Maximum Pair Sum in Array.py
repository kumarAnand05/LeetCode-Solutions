class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        c=sorted(nums)

        return max((c[x]+c[-(x+1)]) for x in range(len(nums)//2))
