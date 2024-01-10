num1 = input("ener num1")
num2 = input("ener num2")


n = len(num1)
m = len(num2)
max_length = max(n, m)

num1 = num1.rjust(max_length, '0')
num2 = num2.rjust(max_length, '0')

carry = 0
add = []

for i in range(max_length - 1, -1, -1):
    digit_sum = int(num1[i]) + int(num2[i]) + carry
    add.append(str(digit_sum % 10))
    carry = digit_sum // 10

if carry:
    add.append(str(carry))


final_sum = "".join(add[::-1])

print(final_sum)
