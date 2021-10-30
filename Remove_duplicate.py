def remove_dup(nums):

    i=0
    while (len(nums)!=len(set(nums))):

        previous=nums[i]
        next = nums[i+1]

        if previous == next:
            nums.pop(i+1)
        else:
            i=i+1

    print (nums)
    return len(nums)


remove_dup([0,1,1,2,2,3,4])