class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        #picking time= 1/unit
        def glass(s:str) -> bool:
            if 'G' in s:return True
        def metal(s:str) -> bool:
            if 'M' in s:return True
        def paper(s:str) -> bool:
            if 'P' in s:return True
        res=0
        G,M,P=[],[],[]

        if glass(s=garbage[0]):res+=garbage[0].count('G')
        if metal(s=garbage[0]):res+=garbage[0].count('M')
        if paper(s=garbage[0]):res+=garbage[0].count('P')

        for n in range(1,len(garbage)):
            s=garbage[n]
            if glass(s):
                G.append(1)
                res+=s.count('G')
            else:G.append(0)

            if metal(s):
                M.append(1)
                res+=s.count('M')
            else:M.append(0)

            if paper(s):
                P.append(1)
                res+=s.count('P')
            else:P.append(0)

        if 1 in P:
            paper= P[::-1]
            res+= sum(travel[:len(travel)-paper.index(1)])
        if 1 in M:
            metal= M[::-1]
            res+= sum(travel[:len(travel)-metal.index(1)])
        if 1 in G:
            glass= G[::-1]
            res+= sum(travel[:len(travel)-glass.index(1)])    
        return res
        
