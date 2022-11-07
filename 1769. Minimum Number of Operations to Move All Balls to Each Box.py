class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x=[t[0] for t in points]
        x.sort()
        diff=[x[n+1]-x[n] for n in range(len(x)-1)]
        return max(diff)
