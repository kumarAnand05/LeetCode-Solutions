class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set([x for x in nums if x>0])
        if len(s)!=0:
            m= max(s)
            if len(s)==m:
                return m+1
            else:
                for n in range(1,m):
                    if n not in s: return n
        else: return 1
