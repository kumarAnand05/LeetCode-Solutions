class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        out= []
        for n in range(len(nums)):
            out.insert(index[n],nums[n])
        return out
