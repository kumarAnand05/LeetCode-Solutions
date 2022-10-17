class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        out=0
        for n in operations:
            if n[0]=='-' or n[-1]=='-':
                out-=1
            else:
                out+=1
        return out
