class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_dict = {}

        for i, num in enumerate(nums):
            if num in index_dict and i - index_dict[num] <= k:
                return True
            index_dict[num] = i

        return False



# time limit excedding for below code
    
# class Solution:
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     n=len(nums)
    #     for i in range (n):
    #         for j in range (n):
    #             if (nums[i]==nums[j] and i!=j and abs(i-j)<=k):
    #                 return True 