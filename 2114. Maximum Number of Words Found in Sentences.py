class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        t= 0
        for n in sentences:
            r= len(n.split())
            if t<r:
                t=r
        return t
