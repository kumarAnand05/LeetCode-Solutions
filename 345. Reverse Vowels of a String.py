class Solution:
    def reverseVowels(self, s: str) -> str:
        v=[s[x] for x in range(len(s)-1,-1,-1) if s[x] in ['A','E','I','O','U','a','e','i','o','u']]
        out=''
        i=0

        for n in s:

            if n in ['A','E','I','O','U','a','e','i','o','u']:
                out+=v[i]
                i+=1
            else:
                out+=n

        return out
