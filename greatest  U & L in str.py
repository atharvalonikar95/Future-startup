class Solution:
    def greatestLetter(self, s: str) -> str:

        max_letter = ''

        for i in s:
            l = i.lower()
            u = i.upper()
            if l != u and l in s and u in s:
                if i > max_letter:
                    max_letter = i

        return max_letter.upper()
