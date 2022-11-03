class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        def identical(s):
            return len(set(s))==1
        def reflection(p):
            return (p[::-1] in words)

        reflects=[]
        odd_identi=[]
        even_identi=[]
        count_reflects=[]
        unique_list=set(words)

        for n in unique_list:

            if identical(s=n): 
                wc=words.count(n)

                if wc%2==0:
                    even_identi.append(wc)
                else:
                    odd_identi.append(wc)

            elif n not in reflects:
                if reflection(p=n):
                    reflects=reflects+[n,n[::-1]]
                    count_reflects.append(min(words.count(n),words.count(n[::-1])))
        
        res=sum(count_reflects)*4
        
        if len(odd_identi)!=0:
            res+=max(odd_identi)*2
            odd_identi.remove(max(odd_identi))

        count=[x//2 for x in odd_identi if x!=1]

        if len(even_identi)!=0:
            res+=sum(even_identi)*2

        if len(count)!=0:
            res+=sum(count)*4
        
        return res
