class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        l1,b1=ax2-ax1,ay2-ay1
        ar1=abs(l1*b1)
        l2,b2=bx2-bx1,by2-by1
        ar2=abs(l2*b2)
        area=ar1+ar2
        # #overlapping
        xa1=list(range(ax1,ax2+1))
        xa2=list(range(bx1,bx2+1))
        cx=[x for x in xa1 if x in xa2]
        if len(cx)<=1:
            return area
        else:
            ya1=list(range(ay1,ay2+1))
            ya2=list(range(by1,by2+1))
            cy=[y for y in ya1 if y in ya2]
            if len(cy)<=1:
                return area
            else:
                return area-abs((len(cx)-1)*(len(cy)-1))
