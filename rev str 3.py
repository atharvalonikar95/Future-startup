# leetcode solclass Solution:
    def reverseWords(self, s: str) -> str:
        r=[]
        r=s.split()
        print(r)

        for i in range (len(r)):
            r[i]=r[i][::-1]
        print(r)

        s=" ".join(r[::1])
        print(s)
        return s

# normal sol
s = "Let's take LeetCode contest"
r=[]
r=s.split()
print(r)

for i in range (len(r)):
    r[i]=r[i][::-1]
print(r)

s=" ".join(r[::1])
print(s)