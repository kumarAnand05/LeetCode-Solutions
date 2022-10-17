class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        r= []
        for n in accounts:
            r.append(sum(n))
        return max(r)
