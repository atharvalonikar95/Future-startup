class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num=str(num)

        if num=='0':
            return True

        
        elif num[-1]=='0' :
            return False
        else :
            return True
        