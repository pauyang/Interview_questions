

class Solution:
    def maxSubArray(self, nums):
        sub_max = nums[0]
        current_sum = 0

        for n in nums:

            if current_sum < 0:
                current_sum = 0
            current_sum += n

            sub_max = max(current_sum, sub_max)
        return sub_max


nums = [-2,1,-3,4,-1,2,1,-5,4]
s=Solution()
print(s.maxSubArray(nums))