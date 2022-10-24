class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count=0
        for n in range(len(nums)-2):
            if nums[n]+diff in nums and nums[n]+(2*diff) in nums:
                count+=1
        return count
