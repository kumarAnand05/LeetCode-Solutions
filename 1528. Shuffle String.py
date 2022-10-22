class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new= ['']*len(s)
        for n in range(len(s)):
            new[indices[n]]=s[n]
        return ''.join(new)
