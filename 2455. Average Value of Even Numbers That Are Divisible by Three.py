class Solution:
    def averageValue(self, nums: List[int]) -> int:
        li=[x for x in nums if x%6==0]
        if len(li)==0:return 0
        else: return sum(li)//len(li)
