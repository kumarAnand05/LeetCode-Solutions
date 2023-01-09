class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
       return (min([x for x in letters if ord(x)>ord(target)])) if len([x for x in letters if ord(x)>ord(target)])!=0 else letters[0]
