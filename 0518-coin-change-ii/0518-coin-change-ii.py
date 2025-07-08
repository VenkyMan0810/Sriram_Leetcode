class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for i in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(amount + 1):
                coin = coins[i - 1]

                dp[i][j] = dp[i-1][j]

                if j >= coin:
                    dp[i][j] += dp[i][j - coin]

        return dp[n][amount]