class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [x for y, x in sorted(zip([sum(n) for n in mat], list(range(len(mat)))))][:k]
