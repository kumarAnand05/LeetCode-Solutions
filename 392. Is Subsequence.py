class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subLength = len(s)
        pos = 0
        r = ''
        for n in t:
            if pos == subLength:
                break
            if n == s[pos]:
                r+=n
                pos+=1
        return True if r==s else False 
