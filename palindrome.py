class Solution:
    
    def isPalindrome(self, x):
        if x < 0:
            return False

        out = []
        

        while x > 0:
            k = x % 10
            out.append(k)
            x = x // 10

        n = len(out)

        if n == 1 and x == 0:
            return True

        for i in range(0, n // 2):
            if out[i] != out[n - 1 - i]:
                return False

        return True
sol=Solution()
print(sol.isPalindrome(0))



       






        