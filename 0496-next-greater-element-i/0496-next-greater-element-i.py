class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        maps = {}

        for i in nums2:
            while stack and i > stack[-1]:
                prev = stack.pop()
                maps[prev] = i
            stack.append(i)

        while stack:
            maps[stack.pop()] = -1

        return [maps[i] for i in nums1]
            
