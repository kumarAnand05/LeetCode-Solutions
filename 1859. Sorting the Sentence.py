class Solution:
    def sortSentence(self, s: str) -> str:
        sl= s.split()
        x= ['#']*len(sl)
        for n in sl:
            x[int(n[-1])-1]=n[:len(n)-1]
            
        return ' '.join(x)
