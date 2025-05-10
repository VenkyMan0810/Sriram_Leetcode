class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ind = []
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i!=j and nums[i] + nums[j] == target:
        #             return [i,j]

        numMap = {}
        n = len(nums)

        # for i in range(n):
        #     numMap[nums[i]] = i

        for i in range(n):
            comp = target - nums[i]
            if comp in numMap:
                return [numMap[comp],i]
            numMap[nums[i]] = i

        return []