class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.lstrip()
        s=s.rstrip()
        print(s)
        s=s.split()
        print(s)
        s=' '.join(s[::-1])
        return s