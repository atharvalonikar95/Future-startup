class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        l=[]
        for i in nums1:
            for j in nums2:
                if i==j:
                    if i not in l:
                        l.append(i)
        return l
            

        