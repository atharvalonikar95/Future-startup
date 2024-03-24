class Solution:
    def countVowelStrings(self, n: int) -> int:
        return self.combination(n + 5 - 1, n)

    def combination(self, n: int, k: int) -> int:

        result = 1
        for i in range(k):
            result *= (n - i)
            result //= (i + 1)
        return result




        