class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)

        for i in range(len(nums)-1):
            j=i+1
            if nums[i]==nums[j]:
                nums[i]*=2
                nums[j]=0
        for i in range (len(nums)):
            if nums[i]==0:
                nums.append(nums[i])
                nums.remove(nums[i])
        return nums