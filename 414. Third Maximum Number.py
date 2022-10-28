class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x= sorted(set(nums))
        if len(x)>2:return x[-3]
        else:return x[-1]


# Alternative one line code:
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        return [sorted(set(nums))[-x] for x in range(1,len(set(nums))+1) if len(set(nums))<3 or x==3][0]
"""
