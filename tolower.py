class Solution:
    def toLowerCase(self, s: str) -> str:
        lowstr=""
        for i in s:
            if i.isupper()==True:
                lowstr+=i.lower()
            else:
                lowstr+=i
        return lowstr
        