class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = []
        i = 1
        while len(l) < k:
            if i not in arr:
                l.append(i)
            i += 1

        return l[-1]


# num=[2,3,4,7,11]
# k=5
# l=[]
# for i in range(1,(num[-1]+k)):
#     if i  not in  num:
#        l.append(i)
# print(l)



# for i in range(len(l)):
#     val=l[k-1]
# print(val)


