class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        r=max(candies)
        out=[]
        for n in candies:
            out.append(n+extraCandies>=r)
        return out
