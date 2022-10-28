class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        x= sum([1 for n in range(len(s)) if s[n]!=goal[n]])==2
        if s==goal:
            if len(set(s))-len(s)!=0: return True
            else: return False
        elif ''.join(sorted(list(s)))!=''.join(sorted(list(goal))): return False
        else: return x
            # daab daab -----  dabe 
            
