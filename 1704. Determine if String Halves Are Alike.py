class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return len([x for x in s[:(len(s)//2)] if x in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U']])==len([x for x in s[(len(s)//2):] if x in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U']])
