class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1

        while (low <= high):

            mid = (low + high) // 2

            if (matrix[mid][-1] < target):
                low = mid + 1
            elif (matrix[mid][0] > target):
                high = mid - 1
            else:
                low_inner = 0
                high_inner = len(matrix[mid]) - 1
                while (low_inner <= high_inner):
                    mid_inner = (low_inner + high_inner) //2
                    if (matrix[mid][mid_inner] < target):
                        low_inner = mid_inner + 1
                    elif (matrix[mid][mid_inner] > target):
                        high_inner = mid_inner - 1
                    else:
                        return True
                return False
        return False
