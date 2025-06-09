class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1

        while begin <= end:
            midpoint = begin + (end-begin) // 2
            mid_val = nums[midpoint]

            if mid_val == target:
                return midpoint

            elif target < mid_val:
                end = midpoint - 1

            else:
                begin = midpoint + 1

        return -1

