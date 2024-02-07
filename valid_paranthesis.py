
class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {'{': '}', '[': ']', '(': ')'}
        stack = []

        for i in s:
            if i in "{[(":
                stack.append(i)
            elif i in ")}]":
                if len(stack)==0 or valid_pairs[stack.pop()] != i:
                    return False
        if len(stack)==0:
            return True
