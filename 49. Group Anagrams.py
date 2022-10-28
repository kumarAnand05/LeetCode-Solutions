class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=[]
        final=[]
        for n in strs:
            an=''.join(sorted(list(n)))
            if an not in anagram:
                anagram.append(an)
                final.append([n])
            else:final[anagram.index(an)].append(n)
        return final
