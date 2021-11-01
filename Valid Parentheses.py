'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
'''


class Solution:
    def isValid(self, s: str) -> bool:
        close_parenthesis={')':'(',']':'[','}':'{'}
        stack = []

        for check in s:
            if stack and check in close_parenthesis.keys():
                if stack[-1]==close_parenthesis[check]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(check)





        return True if not stack else False

st=  "()[]{}"
#st= "([)]"
s=Solution()
t= s.isValid(st)
print(t)