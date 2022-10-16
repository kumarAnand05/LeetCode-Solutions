class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out= ''
        r= min(strs, key=len)
        flag=0
        for n in range(len(r)):
            for p in strs:
                app= True
                curr= strs[0][n]
                if p[n]!=curr:
                    flag=1
                    app= False
                    break
            if app==True:
                out+=curr
            if flag==1:
                break
        return out