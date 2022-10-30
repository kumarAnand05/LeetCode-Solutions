class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        digits= list(map(int,list(str(n))))
        if sum(digits)<=target:return 0
        elif digits[0]>=target: return int('1'+str(0)*len(digits))-n
        else:
            it=0
            place=0
            for n in digits:
                check= it+n
                if check>=target:
                    break
                else:
                    it+=n
                    place+=1
            band=int('1'+str(0)*(len(digits)-place))
            ded=''.join(list(map(str,digits[place:])))
            return band-int(ded)
