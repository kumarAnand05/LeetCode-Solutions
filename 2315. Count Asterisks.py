class Solution:
    def countAsterisks(self, s: str) -> int:
        l= s.split('|')
        count=0
        for n in range(0,len(l),2):
            count+=l[n].count('*')
        return count
