class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        else:
            new=sorted(nums)
            val=0
            for n in range(len(new)-1):
                a=new[n]
                b=new[n+1]
                if (b-a)>val:
                    val=(b-a)
            return val
