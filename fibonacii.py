# using recursion
class Solution:
    def fib(self, n: int) -> int:
        if n ==0 or n==1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)
         

# using non recursive method
class Solution:
    def fib(self, n: int) -> int:
        if n ==0 or n==1:
            return n
        else:
            fib_seq = [0] * (n + 1)
            fib_seq[1] = 1
            print(fib_seq)

            for i in range(2, n + 1):
                fib_seq[i] = fib_seq[i - 1] + fib_seq[i - 2]

            return fib_seq[n]
         
        