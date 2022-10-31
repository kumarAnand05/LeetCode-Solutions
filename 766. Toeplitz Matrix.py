class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        base_row=matrix[0]
        trim=len(matrix[0])-1
        for n in range(1,len(matrix)):
            sample=(base_row)[:trim]
            correct= matrix[n][:1]+sample
            if correct==matrix[n]:
                base_row=matrix[n]
            else:
                return False
                break
        return True
