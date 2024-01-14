from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)

        for i, freq in t_count.items():
            if i not in s_count or s_count[i] != freq:
                return i


solution = Solution()
result = solution.findTheDifference("abcd", "abcde")
print(result)
