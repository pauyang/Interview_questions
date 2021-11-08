'''

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_num1 = self.str_to_int_map(num1)
        print (int_num1)
        int_num2 = self.str_to_int_map(num2)

        return str(int_num1 * int_num2)

    def str_to_int_map(self, num):
        stack = []

        for i in num:
            if i == '0':
                stack.append(0)
            elif i == '1':
                stack.append(1)
            elif i == '2':
                stack.append(2)
            elif i == '3':
                stack.append(3)
            elif i == '4':
                stack.append(4)
            elif i == '5':
                stack.append(5)
            elif i == '6':
                stack.append(6)
            elif i == '7':
                stack.append(7)
            elif i == '8':
                stack.append(8)
            elif i == '9':
                stack.append(9)

        value = 0
        for i, val in enumerate(reversed(stack)):
            value += val * pow(10, i)
        return value

num1 = '123'
num2 = '456'
s = Solution()
t = s.multiply(num1,num2)
print(t)