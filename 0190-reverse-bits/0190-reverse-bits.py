class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):  # Loop exactly 32 times
            result = (result << 1) | (n & 1)
            n >>= 1
        return result