# s = "tree"
# data={}
# for i in range(len(s)):
#     count=1
#     for j in range(len(s)):
#         if s[i]==s[j] and i!=j:
#             count+=1
#     data[s[i]]=count
# data=dict(sorted(data.items(), key=lambda x: x[1],reverse=True))
# print(data)
    
# l=[]
# for i,j in data.items():
#     l.append(i*(j))
# print(l)
# str=''.join(l[::1])
# print(str)

# s = "tree"
# l=[]

# def count(char):
#     return s.count(i)
# max_count=count(0)
# for i in (s):
#     if count(i)>max_count:
#         l.append(i*(count(i)))
        

#     # occ=count(i)
# print(l)
# s = "tree"
# l = []

s = "tree"
result = []

def count(char):
    return s.count(char)

max_count = max(count(char) for char in s)

for char in s:
    if count(char) <= max_count and char not in result:
        result.append(char*(count(char)))

print(result)
print(max_count)

