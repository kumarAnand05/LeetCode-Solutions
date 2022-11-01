class Solution:
    def reverse(self, x: int) -> int:
        r=str(x).strip('-')
        res=r[::-1]
        if x==0:return 0
        else:
            res=int(res.strip('0'))
            if str(x)[0]=='-':
                res=res*(-1)
            if res not in range(-2**31,(2**31)-1):return 0
            else:return res
