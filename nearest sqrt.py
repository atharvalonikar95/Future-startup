import math
class Solution:
    def mySqrt(self, x: int) -> int:
        y=math.sqrt(x)
        z=math.floor(y)
        return z 
num=int(input("Enter number : "))
print(Solution().mySqrt(num))