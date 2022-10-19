class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        t= []
        for n in sentences:
            t.append(len(n.split()))
        return max(t)
