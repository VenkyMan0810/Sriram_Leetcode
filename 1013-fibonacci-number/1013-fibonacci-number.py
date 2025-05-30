class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def recursive(n):
            if n <= 1:
                return n
            else:
                return recursive(n-1) + recursive(n-2)

        return recursive(n)