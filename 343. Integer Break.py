class Solution:
    def integerBreak(self, n: int) -> int:
        if (n==3 or n==2):
            return n-1

        if n%3==0:
            return 3**(n//3)
        elif n%3==1:
            return 3**((n-4)//3)*4
        else:
            return 3**(n//3)*2
