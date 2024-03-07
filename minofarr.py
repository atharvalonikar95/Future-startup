class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        min1=float('+inf')
        for i in range(len(nums)):
            if nums[i]<=min1:
                min1=nums[i]
                break
        return min1