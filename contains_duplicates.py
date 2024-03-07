class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       
        nums=Counter(nums)
        for i,count in nums.items():
            if nums[i]>1:
                return True
        
        