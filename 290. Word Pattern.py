class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li= s.split()
        container=[]
        formation=''
        if len(pattern)==len(li) and len(set(pattern))==len(set(li)):
            for n in range(len(pattern)):
                if pattern[n] not in container:
                    container.append(pattern[n])
                    formation+= li[n]+' '
                else:
                    formation+= li[pattern.index(pattern[n])]+' '
            if formation.strip()==s:
                return True
            else: return False

        else: return False
