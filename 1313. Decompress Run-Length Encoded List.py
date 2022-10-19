class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out=[]
        for n in range(0,len(nums),2):
            out+= [nums[n+1]]*nums[n]
        return out
