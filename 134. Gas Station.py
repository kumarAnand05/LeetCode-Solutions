class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff=[(g-c) for (g,c) in zip(gas,cost)]
        if sum(diff)>=0:
            start_pos=0
            tank=0
            for n in range(len(gas)):
                fuel=gas[n]-cost[n]
                tank+=fuel
                if tank<0:
                    start_pos=n+1
                    tank=0
            return start_pos
        else:
            return -1
