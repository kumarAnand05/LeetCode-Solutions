class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        loop= len(strs[0])
        count=0
        for p in range(loop):
            col=[]
            for n in strs:
                col.append(n[p])
            if col!=sorted(col): count+=1
        return count
            
