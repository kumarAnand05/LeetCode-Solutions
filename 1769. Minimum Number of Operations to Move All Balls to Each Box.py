class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ids=[x for x in range(len(boxes)) if boxes[x]=='1']
        return [sum([abs(x-n) for x in ids]) for n in range(len(boxes))]
