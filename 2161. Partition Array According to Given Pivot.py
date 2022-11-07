class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return [x for x in nums if x<pivot]+[pivot]*(nums.count(pivot))+[t for t in nums if t>pivot]
