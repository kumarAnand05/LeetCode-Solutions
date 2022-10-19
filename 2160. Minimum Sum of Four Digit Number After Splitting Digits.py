class Solution:
    def minimumSum(self, num: int) -> int:
        r= list(str(num))
        r.sort()
        out= int(r[0]+r[-1])+ int(r[1]+r[-2])
        return out
