class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def ways(s):
            if s in memo:
                return memo[s]
            if s <=1:
                return 1
            else:
                res = ways(s-1) + ways(s-2)

            memo[s] = res
            return res
        return ways(n)