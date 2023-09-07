class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = min(len(word1),len(word2))
        final = ''
        for n in range(s):
            final+= word1[n]+word2[n]
        
        final+=word1[s:]+word2[s:]
        return final
