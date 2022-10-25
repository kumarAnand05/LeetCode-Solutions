class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return len([n for n in words if len(set(n).difference(set(allowed)))==0])
