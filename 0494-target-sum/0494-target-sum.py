class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total or (total + target) % 2 == 1:
            return 0

        s = (total + target) // 2


        dp = [0] * (s + 1)
        dp[0] = 1

        for i in nums:
            for j in range(s, i - 1, -1):
                dp[j] += dp[j - i]

        return dp[s]