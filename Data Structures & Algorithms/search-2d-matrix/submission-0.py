class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        double binary search the matrix and then run a binary search on the correct line within the target
        '''
        ROWS, COLS = len(matrix), len(matrix[0])
        low, high = 0, ROWS - 1
        while low <= high:
            row = (low + high) // 2
            if target > matrix[row][-1]:
                low = row + 1
            elif target < matrix[row][0]:
                high = row - 1
            else:
                break
        if not low <= high:
            return False
        
        row = (low + high) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False




