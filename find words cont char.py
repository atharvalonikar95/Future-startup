words=["leet","code"]
x='e'
l=[]
for i in range (len(words)):
    if x in words[i]:
        l.append(i)
print(l)

# for leetcode solution
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l=[]
        for i in range(len(words)):
            if x in words[i]:
                l.append(i)
        return l

                