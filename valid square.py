class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        sqr = math.sqrt(num)
        sqr=str(sqr)

        pt=sqr.index('.')+1
        
        if sqr[-1]=='0' :
            return True
        else:
            return False
        
    

        









# num=681
# import math
# sqr=math.sqrt(num)
# print(sqr)
# print(type(sqr))
# sr=str(sqr)

# print(type(sr))

# pt=sr.index('.')+1
# print(pt)
# print(sr[pt])
# if sr[-1]=='0':
#     print("true")
# else:
#     print("false")
