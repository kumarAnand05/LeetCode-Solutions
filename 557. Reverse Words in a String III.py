class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([n[len(s)::-1] for n in s.split(' ')])
