# # # # print(2**30)

# # # # #1534236469
# # # # #2147483647

# str="abhinandan anil ambekar"
# # str="abcb"
# dic={}
# for i in range(len(str)):
#     count=1
    
#     for j in range(len(str)):
#         if str[i]==str[j] and i!=j:
#             count+=1
#     dic[str[i]]=count
# print(dict(sorted(dic.items())))

# max_item,max_val=None,0
# for i,val in dic.items():
#     if val>max_val:
#        max_val=val
#        max_item=i
# print(max_val)      
# print(max_item)


# # for i i

# # # n=10

# # # print(int((n*(n-1))/2))

# # # print(type(n))

# # str="a-bc-def-ghij"
# # list1=[]
# # for i in str:
# #     list1.append(i)
# # print(str)
# # n=len(list1)
# # # for i in range (n//2):

# # #     for j in range(n-1,(n//2)-1,-1):

                    
# # #         if list1[i]!='-' and list1[j]!='-':
# # #             temp=list1[i]
# # #             list1[i]=list1[j]
# # #             list1[j]=temp
      
# # i,j=0,n-1
# # while i<j:
# #     while(i<j and list1[i]=='-'):
# #         i+=1
# #     while(i<j and list1[j]=='-'):
# #         j-=1
# #     if i<j:
# #             temp=list1[i]
# #             list1[i]=list1[j]
# #             list1[j]=temp
# #             i+=1
# #             j-=1


# # result_str = ''.join(list1)
                   
# # print(result_str)

# # l = [1, 's']

# # for i in range(len(l)):
# #     if type(l[i]) != str:
# #         print(l[i])
# nums=[]
# def add(num):
    
#     num=str(num)
    

#     for i in num:
#         nums.append(int(i))
#     # print(nums)
#     # print(len(nums))

#     sum=0
#     for i in range(len(nums)):
#         sum=sum+nums[i]
#     nums.clear()
#     # print(nums)
#     return sum
# print(add(32))
# if len(str(add(32)))>1:
#     print(add(add(32)))

# from collections import Counter
# nums=[1,2,2,2]

# ele_count=Counter(nums)
# print(ele_count[2])
# # for i,count in ele_count.items():
# #     if ele_count[i]>1:
# #         print(True)
    
# # else:
# #      print(False)
# print(type(nums))

# nums = [5,0,3,5,1]
# nums.sort()
# print(nums)
# for i in range(len(nums)):
#     if nums[i]>0:
#         min1=nums[i]
#         break
# print(min1)

# for i in range(len(nums)):
    
#     if nums[i]>0:
#         nums[i]=nums[i]-min1
    
# print(nums)
# nums = [5,0,3,5,1]
# iterations = 0

# while any(nums[i] > 0 for i in range(len(nums))):
#     nums.sort()

#     min1 = None
#     for i in range(len(nums)):
#         if nums[i] > 0:
#             min1 = nums[i]
#             break

#     if min1 is not None:
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 nums[i] = nums[i] - min1

#     iterations += 1
# print(iterations)

# dividend=-2147483648
# divisor=-1

# ans=dividend/divisor
# if ans>((2**31)-1):
#     print((2**31)-1)
# # ans=ans.__trunc__()
# # print(ans)