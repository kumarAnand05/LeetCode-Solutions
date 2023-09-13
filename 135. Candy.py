class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)

        # forward iteration
        for i in range(0, len(ratings)-1):
            if  ratings[i] < ratings[i+1] and candy[i] >= candy[i+1]:
                candy[i+1] = candy[i] + 1
        
        # backward iteration
        for p in range(len(ratings) - 1, 0, -1):
            if ratings[p-1] > ratings[p] and candy[p-1] <= candy[p]:
                candy[p-1] = candy[p] + 1
        
        return sum(candy)
