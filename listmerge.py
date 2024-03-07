k=int(input("enter number of elements in list1 : "))
list1=[]
for i in range(k):
    ele=int(input())
    list1.append(ele)


m=int(input("enter number of elements in list2 : "))
list2=[]
for i in range(m):
    ele=int(input())
    list2.append(ele)




for i in range(len(list2)):
    list1.append(list2[i])
    list1.sort()
list2.clear()
print(list1)
