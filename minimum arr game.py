class Solution:
    def numberGame(self, nums) :
        arr=[]
        while len(nums) >= 2:
            min1 = min(nums)
            nums.remove(min1)
    
            min2 = min(nums)
            nums.remove(min2)
            arr.extend([min2, min1])
            
        return arr
nums=[2,5]
print(Solution().numberGame(nums))

