class Solution:
    def isPalindrome(self, x: int) -> bool:
        xs= list(str(x))
        l= len(xs)
        if l%2==0:
            l=l//2
        else:
            l=(l+1)//2
        for n in range(l):
            res= True
            if xs[n]!=xs[((0-(1+n)))]:
                res= False
                break
        return res
    
