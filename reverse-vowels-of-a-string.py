class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        left, right = 0, len(l) - 1

        while left < right:
            while left < right and l[left].lower() not in vowels:
                left += 1
            while left < right and l[right].lower() not in vowels:
                right -= 1

            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
        rev_vowel_str=''.join(l)
        return rev_vowel_str
        

        