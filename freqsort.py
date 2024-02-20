# nums = [2,3,1,3,2]
# n = len(nums)

# dic = {}
# for i in range(n):
#     count = 1
#     for j in range(n):
#         if i != j and nums[i] == nums[j]:
#             count += 1
#     dic[nums[i]] = count

# l = []
# max_item, max_val = None, 0
# for i, val in dic.items():
#     if val > max_val:
#         max_item = i
#         max_val = val

# for i in range(max_val):
#     l.append(max_item)

# for i, val in dic.items():
#     if i != max_item:
#         for j in range(val):
#             l.append(i)

# print(l[::-1])

nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
n = len(nums)

dic = {}
for i in range(n):
    count = 1
    for j in range(n):
        if i != j and nums[i] == nums[j]:
            count += 1
    dic[nums[i]] = count

l = []
max_item, max_val = None, 0
for i, val in dic.items():
    if val > max_val:
        max_item = i
        max_val = val

for i, val in dic.items():
    if i != max_item:
        for j in range(val):
            l.append(i)

for i in range(max_val):
    l.append(max_item)

print(l)


