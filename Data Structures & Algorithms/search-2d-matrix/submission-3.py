class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        def run_binary_search(array, target):
            l = 0
            r = len(array) - 1

            while l<=r:
                mid = (l + r) // 2

                if target == array[mid]:
                    return True
                elif target > array[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        list_index_l = 0
        list_index_r = len(matrix) - 1

        while list_index_l <= list_index_r:

            mid = (list_index_l + list_index_r) // 2

            if target > matrix[mid][-1]:
                list_index_l = mid + 1
            elif target < matrix[mid][0]:
                list_index_r = mid - 1
            else:
                return run_binary_search(matrix[mid], target) 
        
        return False


        