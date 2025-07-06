class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def rob_house(house):
            n = len(house)
            if n == 0:
                return 0
            if n == 1:
                return house[0]
            
            dp = [0] * n
            dp[0] = house[0]
            dp[1] = max(house[0], house[1])

            for i in range(2,n):
                dp[i] = max(house[i] + dp[i-2], dp[i-1])
            return dp[-1]

        return max(rob_house(nums[:-1]), rob_house(nums[1:]))    


        