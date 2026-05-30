class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j==0:
                    self.sums[i][j] = matrix[i][j]
                else:
                    self.sums[i][j] = matrix[i][j] + self.sums[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total=0
        for row in range(row1, row2+1):
            if col1==0:
                total += self.sums[row][col2]
            else:
                total += self.sums[row][col2] - self.sums[row][col1 - 1]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

