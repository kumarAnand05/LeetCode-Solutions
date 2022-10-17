class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            out=n
        else:
            out = 2*n
        return out
    
