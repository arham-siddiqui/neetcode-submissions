class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix) - 1
        search = []

        # narrow down the row
        while top <= bottom:
            halfway = (top + bottom) // 2
            if target in range(matrix[halfway][0], matrix[halfway][-1]+1):
                search = matrix[halfway]
                break
            if matrix[halfway][0] < target:
                top = halfway + 1
            else:
                bottom = halfway - 1

        left = 0
        right = len(search) - 1

        while left <= right:
            halfway = (left + right) // 2
            if search[halfway] == target:
                return True
            if search[halfway] < target:
                left = halfway + 1
            else:
                right = halfway - 1
        
        return False