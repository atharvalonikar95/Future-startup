class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        while len(nums) >= 2:
            min1 = min(nums)
            nums.remove(min1)
    
            min2 = min(nums)
            nums.remove(min2)
            arr.extend([min2, min1])
            
        return arr

