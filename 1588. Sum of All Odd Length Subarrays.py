class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        out=sum(arr)
        r= []
        for n in range(1,len(arr)+1,2):
            if n!=1:
                i=0
                for p in range(n,len(arr)+1):
                    out+= sum(arr[i:p])
                    i+=1
        return out    
