class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ps,ns,arr=[],[],[]
        for n in nums:(ps if n>0 else ns).append(n)
        for p,n in zip(ps,ns):arr+=[p,n]
        return arr
