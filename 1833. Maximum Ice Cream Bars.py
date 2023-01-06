class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if sum(costs)>=coins:
            costs.sort()
            count=0
            for n in costs:
                if n<=coins:
                    count+=1
                    coins-=n
                else:
                    break
            return count
        else:
            return len(costs)
