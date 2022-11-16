# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        res=False
        lower=1
        upper=n
        out=0
        prev=0
        while not res:
            mean=((lower+upper)//2)
            if mean!=prev:
                prev=mean
            else:
                out=upper
                break
            check=guess(mean)
            
            if check==0:
                out=mean
                res=True
            elif check==1:
                lower=mean
            elif check==-1:
                upper=mean
        return out
