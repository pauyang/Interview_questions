class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while (left <= right):
            mid = left +(right-left)//2
            if mid*mid >x:
                right = mid-1
            elif mid*mid <x:
                left = mid+1
            else:
                return mid

        return min(right,left)

        '''
        #newton method
        result = x
        while not result * result - x < 1:
            result = (result + x / result) / 2
        return int(result)
        '''

'''
binary search method

        left = 0
        right = x

        while (left <= right):
            mid = left +(right-left)//2
            if mid*mid >x:
                right = mid-1
            elif mid*mid <x:
                left = mid+1
            else:
                return mid

        return right
'''


s=Solution()
print(s.mySqrt(5))