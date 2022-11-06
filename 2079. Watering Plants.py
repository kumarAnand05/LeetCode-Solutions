class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps=0
        can=capacity
        for n in range(len(plants)):
            steps+=1
            if can>=plants[n]:can-=plants[n]
            
            if n!=len(plants)-1 and can<plants[n+1]:
                steps+=(n+1)*2
                can=capacity

        return steps
