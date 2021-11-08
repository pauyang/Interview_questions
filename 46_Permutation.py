'''

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''


class Solution:
    def permute(self, nums):
        stack =[]
        perm=[]

        def backtracking(i,nums):
            stack.append(i)

            if len(stack) == len(nums):
                perm.append(stack[:])
                return

            for val in nums:
                if val not in stack:
                    backtracking(val,nums)
                    stack.pop()



        for i in nums:
            backtracking(i,nums)
            stack.pop()



        return perm




nums = [0,1]
s = Solution()
t = s.permute(nums)
print(t)
