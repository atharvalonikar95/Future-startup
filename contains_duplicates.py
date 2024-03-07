class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums2=[]
        # for i in range(len(nums)):
        #     if nums[i] not in nums2:
        #         nums2.append(nums[i])
        #     elif nums[i] in nums2:
        #         return True
        nums=Counter(nums)
        for i,count in nums.items():
            if nums[i]>1:
                return True
        
        