class Solution:
    def makeGood(self, s: str) -> str:
        flag=0
        r=list(s)
        while r:
            limit=len(r)
            ids=0
            for n in range(limit):
                if n+1<=limit-1 and abs(ord(r[n])-ord(r[n+1]))==32:
                    r.pop(n)
                    r.pop(n)
                    break
                else:
                    ids+=1
                if ids==limit:
                    flag=1
            if flag==1:
                break
        return ''.join(r)
