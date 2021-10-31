
class Solution:
    def findKthLargest(self, nums, k) :
        new_nums = self.quck_sort(nums)
        return new_nums[-k]




    def quck_sort(self,nums):



        if len(nums)> 1:
            pivot = nums.pop()
            less = []
            more = []
            equal = [pivot]



            for i in nums:
                if i > pivot:
                    more.append(i)
                elif i < pivot:
                    less.append(i)
                else:
                    equal.append(i)

            return self.quck_sort(less)+equal+self.quck_sort(more)

        else:
            return nums


nums = [3,2,1,5,6,4]
k = 2

s= Solution()
t=s.findKthLargest(nums,k)
print (t)