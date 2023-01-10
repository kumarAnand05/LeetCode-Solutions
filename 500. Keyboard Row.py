class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return [x for x in words if len(set(list(x.lower())).difference(set(list('asdfghjkl'))))==0 or len(set(list(x.lower())).difference(set(list('qwertyuiop'))))==0 or len(set(list(x.lower())).difference(set(list('zxcvbnm'))))==0]
