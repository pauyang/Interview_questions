class Solution:
    def threeSum(self, nums):

        #edge case handling
        if not nums:
            return []
        if len(nums)<=2:
            return []

        #Use set to remove duplicate and then sort the list

        new= list(nums)
        new.sort()

        #initiate result:
        result = []



        #Iterate through length num -2
        for i in range(len(new)-2):

            # Initiate left and right ptr
            left = i+1
            right = len(new)-1

            #move right ptr if result > 0
            #move left ptr if result  < 0
            #Append to result if ==0 and increment left, decrement right (avoid duplicate)
            #halt when left ptr cross right ptr
            #save result as tuple so we can use set to remove duplicate

            while(left < right):
                res= new[i]+new[left]+new[right]
                if res > 0:
                    right -=1

                elif res < 0:
                    left+=1

                else:
                    result.append(tuple([new[i], new[left],new[right]]))
                    left+=1
                    right-=1


        return list(set(result))











s = Solution()
t = s.threeSum([-2,0,1,1,2])
print (t)