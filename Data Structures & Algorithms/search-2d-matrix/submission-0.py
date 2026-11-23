class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left , right = 0, (len(matrix) * len(matrix[0]) - 1)
        while left <= right:
            middle = (left + right)//2
            # we have to convert the middle index into a value#
            row = middle // len(matrix[0])
            col = middle % len(matrix[0])
            value = matrix[row][col]
            if target == value :
                return True
            elif target < value:
                right = middle - 1
            else:
                left = middle + 1
        return False

            