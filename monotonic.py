class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n=len(nums)
        
        if n <= 1:
            return True 
        
        incr = decr = True
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                decr = False
            elif nums[i] < nums[i - 1]:
                incr = False
        
        return incr or decr



        