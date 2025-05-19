class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        left, right = 0, len(height) - 1

        while left < right:
            Hleft = height[left]
            Hright = height[right]
            width = right - left

            area = min(Hleft, Hright) * width

            max_area = max(max_area, area)

            if Hleft < Hright:
                left += 1
            else:
                right -= 1

        return max_area