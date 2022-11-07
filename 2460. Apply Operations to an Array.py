class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        t=0
        container=[]
        while t<=len(nums)-1:
            if t!=len(nums)-1 and nums[t]==nums[t+1]:
                if nums[t]!=0:
                    container.append(nums[t]*2)
                t+=1
            else:
                if nums[t]!=0:
                    container.append(nums[t])
            t+=1
        return container+([0]*(len(nums)-len(container)))
                
