class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        o= sorted(heights, reverse=True)
        return [names[heights.index(x)] for x in o]
