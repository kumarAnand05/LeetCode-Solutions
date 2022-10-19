class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        r= list(map(int, list(str(n))))
        t= sum(r)
        p= 1
        for n in r:
            p*=n
        return p-t
