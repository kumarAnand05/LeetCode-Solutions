class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        x=sorted([t[0] for t in points])
        return max([x[n+1]-x[n] for n in range(len(x)-1)])
