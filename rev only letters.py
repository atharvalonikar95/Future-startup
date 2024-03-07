class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        list1=[]
        for i in s:
            list1.append(i)
        i, j = 0, len(list1) - 1

        while i < j:
            while i < j and not list1[i].isalpha():
                i += 1
            while i < j and not list1[j].isalpha():
                j -= 1

            if i < j:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
                i += 1
                j -= 1

        revStr = ''.join(list1)
        return revStr
print(Solution().reverseOnlyLetters("hello"))