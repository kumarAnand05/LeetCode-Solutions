class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        r= list(set(nums))
        count=0
        for n in range(len(r)):
            if r[n]+k in r: count+= (nums.count(r[n]))*(nums.count(r[n]+k))
        return count
