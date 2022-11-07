class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        def offgrid(c,pos):   
            if (c=='R' or c=='D') and (pos+1<=limit):return pos+1
            elif (c=='L' or c=='U') and pos-1>=0:return pos-1
            else:return -1
            
        res=[]
        limit=n-1

        for n in range(len(s)):
            count=0
            segment=s[n:]
            x_pos=startPos[0]
            y_pos=startPos[1]
            for n in segment:
                if n=='R' or n=='L':
                    t=offgrid(c=n,pos=y_pos)
                    if t!=-1:
                        y_pos=t
                        count+=1
                    else:break
                elif n=='D' or n=='U':
                    t=offgrid(c=n,pos=x_pos)
                    if t!=-1:
                        x_pos=t
                        count+=1
                    else:break

            res.append(count)

        return res
                
