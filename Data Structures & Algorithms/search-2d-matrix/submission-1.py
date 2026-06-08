class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])

        # find the row
        t, b = 0, rows - 1
        while t <= b:
            mid = ((b - t) // 2) + t
            if matrix[mid][0] <= target and matrix[mid][columns - 1] >= target:
                # search by array here
                return self.binary_search(matrix[mid], target=target)
            elif matrix[mid][0] > target:
                b = mid - 1
            else:
                t = mid + 1

        return False

    def binary_search(self, arr: List[int], target: int) -> bool:
        n = len(arr)
        l, r = (0, n - 1)
        print(arr)
        while l <= r:
            mid = ((r -l ) // 2) + l
            if arr[mid] < target :
                l = mid + 1
            elif arr[mid] > target:
                r = mid - 1
            else :
                return True
        return False
