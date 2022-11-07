class Solution:
    def maximum69Number (self, num: int) -> int:
        s=list(str(num))
        if '6' in s:
            r=s.index('6')
            s[r]='9'
        return ''.join(s)
