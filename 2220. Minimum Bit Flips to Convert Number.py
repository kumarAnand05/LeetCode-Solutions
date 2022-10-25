class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #converting numbers to binary
        def binary(num: int) -> int:
            bv=''
            while num!=0:
                bv+=str(num%2)
                num=num//2
            return bv[::-1]
            
        sbv= binary(num=start)
        gbv= binary(num=goal)
        count=0
        #equalizing lenght of binary numbers
        if len(gbv)!=len(sbv):
            pre='0'*(abs(len(gbv)-len(sbv)))
            if len(gbv)>len(sbv):
                sbv= pre+sbv
            else:
                gbv= pre+gbv
        # iterating through each binary number
        for n in range(len(sbv)):
            if sbv[n]!=gbv[n]:
                count+=1
        return count

        
