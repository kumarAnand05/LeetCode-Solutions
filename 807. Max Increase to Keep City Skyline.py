class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        def colmax(col:int):
            return max([grid[x][col] for x in range(len(grid))]) 

        col_limit= [colmax(col) for col in range(len(grid[0]))]
        out=0

        for n in range(len(grid)):
            row=grid[n]
            row_limit=max(row)

            for i in range(len(row)):
                if row[i]!=row_limit:
                    out+=min([row_limit,col_limit[i]])-row[i]

        return out
