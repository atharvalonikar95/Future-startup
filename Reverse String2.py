str="abcdef"

l=[]
for i in range (len(str)):
    l.append(str[i])
print(l)


k=2
l=l[(k)::-1]

print(l)

# if 2*k <len(str):
#     for i in range(2*(k),2*(k)+1):
#         l[i],l[i+1]=l[i+1],l[i]
# print(l)




