class Solution:
    def twoSum(self, nums, target: int):
        hash = {} #key is value, value is index

        for i in range(len(nums)):
            value = target-nums[i]
            if value in hash.keys():
                return [hash[value],i]

            else:
                hash[nums[i]]=i

'''
#brute force
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target == nums[i]+nums[j]:
                    return [i,j]
'''


s = Solution()
t = s.twoSum([3,2,4],6)
print (t)