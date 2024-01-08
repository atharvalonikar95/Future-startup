s = "pwwkew"
n = len(s)
sublen = 0
char = set()
l = 0

for r in range(n):
    if s[r] not in char:
        char.add(s[r])
        sublen = max(sublen, r - l + 1)
    else:
        while s[r] in char:
            char.remove(s[l])
            l += 1
        char.add(s[r])

print(sublen)


