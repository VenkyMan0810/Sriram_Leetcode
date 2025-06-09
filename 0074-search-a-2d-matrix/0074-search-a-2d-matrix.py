class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # if not matrix or not matrix[0]:
        #     return False

        for i in matrix:
            begin, end = 0, len(i) - 1

            while begin <= end:
                mid = (begin + end)//2
                if i[mid]==target:
                    return True

                elif i[mid] < target:
                    begin = mid + 1
                else:
                    end = mid - 1

        return False
           