
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


'''

# #Open and # Close are equal
# #Close<#Open
# Always start with open
#  Valid if n==close==open


class Solution:
    def generateParenthesis(self, n):

        stack =[]
        res = []

        def backtracking(Nopen,Nclose):

            if Nopen ==Nclose==n:
                res.append(''.join(stack))
                return

            if Nopen<n:
                stack.append('(')
                backtracking(Nopen+1,Nclose)
                stack.pop()

            if Nclose<Nopen:
                stack.append(')')
                backtracking(Nopen,Nclose+1)
                stack.pop()

        backtracking(0,0)

        return res





st=3
s = Solution()
t = s.generateParenthesis(st)
print(t)