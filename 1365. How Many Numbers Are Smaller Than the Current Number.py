import copy
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new=sorted(nums)
        return [new.index(x) for x in nums]

