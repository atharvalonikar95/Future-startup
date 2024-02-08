class Solution:
    def reverseString(self, s: List[str]) -> None:
        p=[]
        for i in range(len(s)):
            p.append(s[i])
        s.clear()
        for i in range (len(p)-1,-1,-1) :
            s.append(p[i])
            