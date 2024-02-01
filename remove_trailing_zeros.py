class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        s=[]
        for i in num:
            s.append(i)
        for i in s:
            while s[-1]=='0':
                s.pop()
        num=''.join(s)
        return num