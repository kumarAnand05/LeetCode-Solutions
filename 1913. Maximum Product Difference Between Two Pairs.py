class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        li=[]
        for n in range(2):
            ma=max(nums)
            li.append(ma)
            nums.remove(ma)
            mi=min(nums)
            li.append(mi)
            nums.remove(mi)
        return (li[0]*li[2])-(li[1]*li[-1])
