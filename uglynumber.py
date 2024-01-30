class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        prime_facts=[2,3,5]
        for i in prime_facts:
            while n%i==0:
                n=n/i
        if n==1:
            return True

