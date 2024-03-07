
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            nstr = str(n)
            n = 0
            print(s)
            for i in nstr:
                n += int(i) ** 2

        if n==1:
            return True
        else:
            return False
        