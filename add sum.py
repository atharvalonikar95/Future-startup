
class Solution:
    
    
    def addDigits(self, num: int) -> int:
        num = str(num)
        nums=[]

        for i in num:
             nums.append(int(i))

        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]

        
        if sum >= 10:
            
            return self.addDigits(sum)
        else:
            return sum
