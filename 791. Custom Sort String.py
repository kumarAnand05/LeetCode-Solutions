class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order=list(order)
        s=list(s)
        if len(set(order).difference((list(s))))==len(order) or len(s)==1:
            return s
        else:
            check=[]
            other=[]
            for n in s:
                if n in order:
                    check.append(n)
                else: other.append(n)
            out=[]
            for p in order:
                co=check.count(p)
                if co!='':
                    out+= [p]*co
        return ''.join(out+other)
