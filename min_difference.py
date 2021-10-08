
class Solution:
    def minDifference(self, nums) -> int:
        nums.sort()

        if len(nums )<= 3:
            return 0
        else:

            #option1:
            temp=nums[:]
            temp[0] = temp[-1]
            temp[1] = temp[-1]
            temp[2] = temp[-1]
            opt1 = max(temp)-min(temp)

            #option2:
            temp= nums[:]
            temp[-1] = temp[0]
            temp[-2] = temp[0]
            temp[-3] = temp[0]
            opt2 = max(temp)-min(temp)

            #options3:
            temp= nums[:]
            temp[0] = temp[-1]
            temp[1] = temp[-1]
            temp[-1] = nums[0]
            opt3 = max(temp)-min(temp)

            #option4:
            temp = nums[:]
            temp[-1] = temp[0]
            temp[-2] = temp[0]
            temp[0] = nums[-1]
            opt4 = max(temp)-min(temp)

            #option5:
            temp = nums[:]
            temp[-1] = temp[1]
            temp[-2] = temp[1]
            temp[0] =  temp[1]
            opt5 = max(temp)-min(temp)

            #option6:
            temp = nums[:]
            temp[-1] = temp[-2]
            temp[0] = temp[-2]
            temp[1] =  temp[-2]
            opt6 = max(temp)-min(temp)


            return min(opt1,opt2,opt3,opt4,opt5, opt6)

s = Solution()
t = s.minDifference([82,81,95,75,20])
print (t)