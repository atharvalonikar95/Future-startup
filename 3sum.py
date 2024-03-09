from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []

        result = []

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0 and i != j != k:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in result:
                            result.append(triplet)

        return result
