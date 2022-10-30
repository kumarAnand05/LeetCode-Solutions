class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        seats= list(range(len(flowerbed)))
        occ= [x for x in range(1,len(flowerbed)+1) if flowerbed[x-1]==1]
        if n==0: return True
        elif len(occ)==0:
            if len(seats) in range(1,3): return n==1
            else:
                if len(seats)%2==0: return len(seats)//2>=n
                else: return (len(seats)+1)//2>=n
        elif len(occ)==len(flowerbed)-1: return False
        
        else:
            ip=occ[0]-1
            out= ip//(2)
            fp=len(flowerbed)-occ[-1]
            out+= fp//(2)
            for p in range((len(occ)-1)):
                D= occ[p+1]-occ[p]-1
                if D>2:out+= (D-1)//(2)
            return out>=n
