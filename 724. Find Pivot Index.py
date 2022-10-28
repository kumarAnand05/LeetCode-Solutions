class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for n in range(0,len(nums)):
            left= sum(nums[:n])
            right= sum(nums[n+1:])
            if left==right:
                return n
                break
        return -1
