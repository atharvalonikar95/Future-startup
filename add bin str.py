class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0

       
        a = a.zfill(max(len(a), len(b)))
        b = b.zfill(max(len(a), len(b)))

        for i in range(len(a) - 1, -1, -1):
            
            digit_sum = int(a[i]) + int(b[i]) + carry

            carry = digit_sum // 2
            result = str(digit_sum % 2) + result
        if carry:
            result = str(carry) + result

        return result
