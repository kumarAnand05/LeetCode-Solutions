class Solution:
    #--------list item access grid[r][c]
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # wall check
        def wallcheck(r:int,c:int, current_val:int) -> bool:
            #right wall
            if current_val==1 and c==c_limit: #todo current_val and c_limit
                return True
            elif current_val==-1 and c==0:return True
            else:return False
        # v check
        def vcheck(r:int,c:int, current_val:int) -> bool:
            if wallcheck(r,c,current_val):return True
            else:
                if current_val==1:
                    next_val=grid[r][c+1]
                    if next_val!=current_val:return True
                    else:return False
                elif current_val==-1:
                    next_val=grid[r][c-1]
                    if next_val!=current_val:return True
                    else:return False
        
        # main----------------------------------------------
        c_limit=len(grid[0])-1
        out=[]
        for n in range(len(grid[0])):
            c=n
            res=0
            for row in range(len(grid)):
                r=row
                current_val= grid[r][c]
                if vcheck(r,c,current_val):
                    res=-1
                    break
                else:
                    if current_val==1:c+=1
                    else: c-=1
            if res==-1:out.append(res)
            else: out.append(c)
        return out
