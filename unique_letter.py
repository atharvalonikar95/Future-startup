str=input("enter string")
non_matching_letter={}
for i in range(len(str)):
    count=1
    for j in range(len(str)):
        if str[i]==str[j] and i!=j:
            count+=1
        non_matching_letter[str[i]]=count
print(non_matching_letter)

# i,j=None,0
for item,val in non_matching_letter.items():
    if val==1:
        print(item)


# app 2
# str="abcdab"

# for i in str:
#     if str.count(i)<=1:
#         print(i,end=",")
