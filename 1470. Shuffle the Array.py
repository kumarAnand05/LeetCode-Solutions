class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new=[]
        for p in range(n):
            new.append(nums[p])
            new.append(nums[n+p])
        return new
