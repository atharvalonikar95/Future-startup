class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(-31,31):
            if n ==4**i:
                return True